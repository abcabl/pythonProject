import cv2
from xml.etree import ElementTree as ET
def draw_rectangle_by_point(img_file_path,new_img_file_path,xml_path):#画外接矩阵

    l_max = []#定义一个数组，用来保存一张图像所有矩形对应的左上角，右下角的点坐标
    tree = ET.parse(xml_path)
    root = tree.getroot()#拿到根节点
    objects = root.findall("object")#找到所有“obgect",得到一个列表
    for i in objects:#遍历列表，拿到每一个”obgect"
        l_min = []#定义一个小列表，用来存储每个矩形框的左上角，右下角的坐标点，一共四个点
        l_min.append(int(i.find("regionX").text))#左上角x
        l_min.append(int(i.find("regionY").text))#左上角y
        l_min.append(int(i.find("regionWidth").text) + int(i.find("regionX").text))#右下角x
        l_min.append(int(i.find("regionHeight").text) + int(i.find("regionY").text))#右下角y
        l_max.append(l_min)#把小列表追加进大列表

    image = cv2.imread(img_file_path)#读取图像
    for item in l_max:#遍历大列表
        point=item
        first_point=(int(point[0]),int(point[1]))#取出左上角的点坐标
        last_point=(int(point[2]),int(point[3]))#取出右下角的点坐标

        print("左上角：",first_point)
        print("右下角：",last_point)
        cv2.rectangle(image, first_point, last_point, (0, 0,255),2)#在图片上进行绘制框
        # cv2.putText(image, item[0], first_point, cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(255,0,0), thickness=1)#在矩形框上方绘制该框的名称

    cv2.imwrite(new_img_file_path, image)#将新图片保存在指定路径




draw_rectangle_by_point("./train-5/1315/1315.jpg","./save/1315.jpg","./train-5/1315/1315.xml")








