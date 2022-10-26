import cv2
#print(cv2.getVersionString())
image=cv2.imread("./train-5/184/184.jpg")
# print(image.shape[0:3])
cv2.imshow("image",image)
cv2.waitKey()
# from xml.etree import ElementTree as ET
# l_max=[]
#
# tree=ET.parse("./train-5/184/184.xml")
# root=tree.getroot()
# # # print(root)
# # j=0
# # for child in root:
# #     # print(child.tag,child.attrib,child.text)#拿到子节点的信息
# #     for i in child:
# #         if i.tag=='point':
# #             j=j+1
# # # print(f"-------------{j}")
# # for i in root.iter('point'):
# #     print(i.text)
# #     print(f"---------------->{len(i.text)}")
# objects=root.findall("object")
# for i in objects:
#     l_min=[]
#     l_min.append(int(i.find("regionX").text))
#     l_min.append(int(i.find("regionY").text))
#     l_min.append(int(i.find("regionWidth").text)+int(i.find("regionX").text))
#     l_min.append(int(i.find("regionHeight").text) + int(i.find("regionY").text))
#     l_max.append(l_min)
#     # print(l_min)
# # print(l_max)
#
#
#
#
# def draw_rectangle_by_point(img_file_path,new_img_file_path,points):
#     image = cv2.imread(img_file_path)
#     for item in points:
#         # print("当前字符：",item)
#         point=item
#         first_point=(int(point[0]),int(point[1]))
#         last_point=(int(point[2]),int(point[3]))
#
#         # first_point = (point[0] * 2, point[1] * 2)
#         # last_point = (point[2]* 2, point[3] * 2)
#         print("左上角：",first_point)
#         print("右下角：",last_point)
#         cv2.rectangle(image, first_point, last_point, (0, 0,255),2)#在图片上进行绘制框
#         # cv2.putText(image, item[0], first_point, cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(255,0,0), thickness=1)#在矩形框上方绘制该框的名称
#
#     cv2.imwrite(new_img_file_path, image)
#
# draw_rectangle_by_point("./train-5/184/184.jpg","./save/184.jpg",l_max)








