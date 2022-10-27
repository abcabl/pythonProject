import numpy as np
import cv2
from xml.etree import ElementTree as ET

# dd = cv2.imread("./train-5/1312/1312.jpg")
untested_objects = []
'''
以下的contrast函数是一个用于计算实际值与
预测值的查全率(true_count / truth_count)，查准率的函数(true_count / test_count)
'''


def contrast(file_path_xml, test_objects, pixel=10):
    # 解析xml文件
    tree = ET.parse(file_path_xml)
    root = tree.getroot()
    objects = root.findall('object')
    # 获取xml文件中的矩形信息
    groundtruth = []
    # 列表中字典的个数
    test_count = len(test_objects)
    for obj in objects:
        x_position = int(obj.find('regionX').text)
        y_position = int(obj.find('regionY').text)
        width = int(obj.find('regionWidth').text)
        height = int(obj.find('regionHeight').text)
        # 将xml文件信息存入字典列表中
        groundtruth.append({'regionX': x_position, 'regionY': y_position, 'regionWidth': width, 'regionHeight': height})

    truth_count = len(groundtruth)
    true_count = 0
    # 将测试数据和xml文件数据对比
    for obj in test_objects:
        for item in groundtruth:
            if abs(item['regionX'] - obj['regionX']) <= pixel and abs(
                    item['regionY'] - obj['regionY']) <= pixel and abs(
                item['regionWidth'] + item['regionX'] - obj['regionWidth'] - obj['regionX']) <= pixel and abs(
                item['regionHeight'] + item['regionY'] - obj['regionHeight'] - obj['regionY']) <= pixel:
                true_count += 1
                break
    # 返回查全率和查准率
    return [true_count / truth_count, true_count / test_count]

#-------------------------------------------------------------------------------------
# 设置li2用来存储满足条件的轮廓，具体作用见下
li2 = []
# 设置li3用来存储li2
li3 = []

# l1存储了所有要识别图像的路径
l1 = ["./train-5/184/184.jpg", "./train-5/1308/1308.jpg", "./train-5/1310/1310.jpg", "./train-5/1312/1312.jpg",
      "./train-5/1315/1315.jpg"]
# l2存储了所有要识别图像的xml文件路径
l2 = ["./train-5/184/184.xml", "./train-5/1308/1308.xml", "./train-5/1310/1310.xml", "./train-5/1312/1312.xml",
      "./train-5/1315/1315.xml"]


def scanner(num, iterations_, len_):  # 识别函数，num:识别第几张图，iterations_:膨胀迭代次数调节，len_:规定要识别多少边形
    # 读取图像
    a = cv2.imread(l1[num])
    # 读取xml图像
    b = cv2.imread(l1[num])
    # 图像灰度化处理
    find = gray = cv2.imread(l1[num], 0)
    # 将灰度图进行膨胀，以尽可能的使图上单独的没有细胞质的杂志显现出来
    kernel = np.ones((17, 17), np.uint8)
    find = cv2.dilate(find, kernel, iterations=iterations_)  # 调整膨胀参数
    # 图像二值化
    ret, find = cv2.threshold(find, 236, 255, cv2.THRESH_BINARY)
    # 图像模糊化，使显现出来的单独的没有细胞质的杂志像素值升高，即变明亮
    find = cv2.blur(find, (20, 20))
    # 将原灰度图gray与模糊处理后的图像find进行像素值相加(add),由于模糊处理后的杂志的像素值会变得很高，即很亮，故相加后它在图像中会接近于“消失”！，以此来消除杂质
    find = cv2.add(find, gray)  # 进行图像变换处理
    # 图像二值化反转，让背景变黑，待圈出区域变白
    ret1, thresh1 = cv2.threshold(find, 90, 255, cv2.THRESH_BINARY_INV)
    # 寻找轮廓
    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # 每个轮廓信息记录在contours里面
    for cent in contours:
        # epsilon代表在0.001下的精度，数值越小，框出的轮廓约精确，但同时也会带来一些问题
        epsilon = 0.001 * cv2.arcLength(cent, True)
        # approx记录着具体轮廓信息，我们可以通过它判断轮廓是几边形
        approx = cv2.approxPolyDP(cent, epsilon, True)
        #
        # res_ = cv2.drawContours(a, [approx], -1, (0, 0, 255), 2)
        # if len(approx)>25:#30
        # 因为我们需要圈出的细胞核的形状是趋近于椭圆的，它的边数是接近于无穷大，我们只需要给定一个边数下限制来筛出其他边数不符合的轮廓，当然这并不能排除我们会误圈出杂质
        if len(approx) > len_:  # 30
            # li1用来存储所有满足条件的轮廓的区域的x,y,w,h
            li1 = []
            x, y, w, h = cv2.boundingRect(cent)
            li1.append(x)
            li1.append(y)
            li1.append(w)
            li1.append(h)
            # 将每一个li1存入li2中，即将列表存入列表中
            li2.append(li1)
            # cv2.rectangle(dd, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # 遍历li2中的每个值，判断是否有些方框交叉，若有两个方框交叉，则判断他们为被我们误圈进来的杂志，进行二次筛选
    for f in li2:
        for d in li2:
            if d != f:
                zx = abs(f[0] + f[0] + f[2] - d[0] - d[0] - d[2])
                x = abs(f[2]) + abs(d[2])
                zy = abs(f[1] + f[1] + f[3] - d[1] - d[1] - d[3])
                y = abs(f[3]) + abs(d[3])
                if zx <= x and zy <= y:
                    if f not in li3:
                        # li3中存储了所有相互交叉的方框的信息
                        li3.append(f)

    for n in li3:
        # 经与其他方框交叉的方框在原来列表中删除
        li2.remove(n)
        # 遍历li2，圈出我们最终的矩形框
    for i in li2:
        # 列表g用来存储每个符合我们预期的实际矩形框的x,y,w,h,并与期望矩形框在位置上进行对比
        g = {}
        cv2.rectangle(b, (i[0], i[1]), (i[0] + i[2], i[1] + i[3]), (0, 0, 255), 2)
        g["regionX"] = i[0]
        g["regionY"] = i[1]
        g["regionWidth"] = i[2]
        g["regionHeight"] = i[3]
        untested_objects.append(g)


'''
对上面的主方法思路过程梳理总结：
1.图像灰度化，得到图像find，gray
2.find图像膨胀突出杂志
3.find图像二值化
4.find图像模糊化使杂质的像素值变高，即变得更亮
5.find与gray进行像素值相加add,这样得到的效果就是原图中的杂志大部分几乎“消失了”(一次筛选)
6.图像二值化反转，即背景变为黑色，待检测区域为白色
7.进行轮廓检测，记录所有轮廓的变数len
8.细胞核的形状是趋近于椭圆的，它的边数是接近于无穷大，我们给定一个边数下下限，只要边数大于这个下限，我们认为他就是椭圆
9.再对满足边数限制的轮廓的x,y,w,h记录下来，判断其中是否有会交叉的矩形框，并将其排除(二次筛选)
10.将最终的轮廓在原图中画出外接矩形，并记录他们的x,y,w,h，与期望值进行比较，得出查全率，查准率
'''
#-----------------------------------------------------------------------------------
# 进行参数效果比较，将结果写进你给定的文件里
with open("指定一个文件写数据...", "w") as w:
    for iteration in range(5):
        for lens in range(11):
            w.writelines(f"参数-->iteration:{1 + iteration}, len:{20 + lens}" + '\n')
            for i in range(5):
                scanner(i, 1 + iteration, 20 + lens)
                m, n = contrast(l2[i], untested_objects)
                untested_objects.clear()
                li2.clear()
                li3.clear()
                # 舍弃效果过于差的参数
                if m < 0.25 or n < 0.25:
                    w.write("查全率或查准率过低！该参数不适用xxxxxxxxxxxxxxxxx" + '\n')
                    break
                else:
                    w.writelines(f"第{i}张图片识别率如下：" + '\n')
                    w.writelines(f"查全率：{m}" + '\n')
                    w.writelines(f"查准率:{n}" + '\n')
            w.writelines("-------------" + '\n')

cv2.waitKey()
cv2.destroyAllWindows()
