import cv2
from xml.etree import ElementTree as ET
def equal(path1,path2):#判断是否相等的函数
#path1代表图像路径，path2代表xml文件路径
    image = cv2.imread(path1)#"train-5/184/184.jpg"
    tuple=image.shape[0:3]#拿到高，宽，通道数，结果是元组
    # print(image.shape[0:3])
    w=tuple[1]
    h=tuple[0]
    d=tuple[2]

    tree = ET.parse(path2)#"./train-5/184/184.xml"
    root = tree.getroot()#拿到根节点
    width = root.find("size").find("width").text#通过根节点目录一层一层的寻找所需要的元素
    print(f"width={width}")
    height = root.find("size").find("height").text
    print(f"height={height}")
    depth = root.find("size").find("depth").text
    print(f"depth={depth}")

    if w==int(width) and h==int(height)and d==int(depth):
        return True
    else:
        return False

print(equal("train-5/184/184.jpg","./train-5/184/184.xml"))




