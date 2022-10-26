import cv2
import numpy as np

img2=cv2.imread("./train-5/184/184.jpg",cv2.IMREAD_GRAYSCALE)
img=cv2.imread("./train-5/184/184.jpg",cv2.IMREAD_GRAYSCALE)
img3=cv2.imread("./train-5/184/184.jpg")

ret1,dst1=cv2.threshold(img,30,255,cv2.THRESH_TOZERO)#控制阈值
# # ret,dst=cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)#控制阈值--反转
# dst2=dst1-dst
i=img2-dst1
cv2.imshow("process",dst1)
cv2.imshow("yuan",img2)
cv2.imshow("jian",i)#求相减后的图像差
ret,dst=cv2.threshold(i,10,255,cv2.THRESH_BINARY_INV)#控制阈值--反转得到i
# cv2.imshow("4",dst)


l=dst
# gray= cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
ret_, thresh_ = cv2.threshold(l,80, 255, cv2.THRESH_BINARY)
contours_, hierarchy_ = cv2.findContours(thresh_, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for cnt in contours_:#边缘检测
    x,y,w,h=cv2.boundingRect(cnt)
    print(f"w:{w},h:{h}")
    if 70>w>20:
        i=cv2.rectangle(img3,(x,y),(x+w,y+h),(0,0,255),2)
#---------------------------



# img = cv2.imread("./train-5/184/184.jpg")
# # kernel=np.ones((3,3),np.uint8)
# # erosion=cv2.erode(img,kernel,iterations=3)#腐蚀
#
# # l=erosion
# l=img
# gray= cv2.cvtColor(l, cv2.COLOR_BGR2GRAY)
# ret_2, thresh_2 = cv2.threshold(gray,80, 255, cv2.THRESH_BINARY)
# contours_2, hierarchy_2 = cv2.findContours(thresh_2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# for cnt_2 in contours_2:#边缘检测
#     if cnt_2.all() in contours_:
#         continue
#     else:
#         x,y,w,h=cv2.boundingRect(cnt_2)
#         print(f"w:{w},h:{h}")
#         if 70>w>20:
#             i=cv2.rectangle(img3,(x,y),(x+w,y+h),(0,0,0),2)

cv2.imshow("11",img3)






#---------------------------------










# kernel=np.ones((5,5),np.uint8)
# erosion=cv2.erode(dst,kernel,iterations=2)#腐蚀
# cv2.imshow("1",erosion)





# cv2.imshow("r",dst1)
# cv2.imshow("g",dst)
# cv2.imshow("img",img)
# v1=cv2.Canny(img,80,150)
# cv2.imshow("r",v1)
# l=img
# for i in range(100):
#     up=cv2.pyrUp(l)
#     up=cv2.pyrDown(up)
#     l=img-up
# cv2.imshow("r",l)#金字塔处理
cv2.waitKey()
cv2.destroyAllWindows()