from xml.etree import ElementTree as ET
def count(path):#输出细胞数目
    tree = ET.parse(path)  # "./train-5/184/184.xml"
    root = tree.getroot()#拿到根节点
    num=root.find("objCount").text
    return num


print(count("./train-5/184/184.xml"))