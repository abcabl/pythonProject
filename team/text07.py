import cv2
import numpy as np

img = cv2.imread("./train-5/1308/1308.jpg")
img1=cv2.cvtColor(img,cv2.IMREAD_GRAYSCALE)

kernel=np.ones((4,4),np.uint8)
erosion=cv2.erode(img1,kernel,iterations=2)#腐蚀

v1=cv2.Canny(erosion,10,20)
# cv2.imshow("1",v1)

# kernel=np.ones((3,3),np.uint8)
# dilate=cv2.dilate(v1,kernel,iterations=4)



contours, hierarchy = cv2.findContours(v1 , cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# draw=img.copy()
# res=cv2.drawContours(draw,contours,-1,(0,255,0),2)



for cnt in contours:#边缘检测
    x,y,w,h=cv2.boundingRect(cnt)
    print(f"w:{w},h:{h}")
    if w > 60 and h>30:
        i=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)


# for cent in contours:
#     epsilon=0.1*cv2.arcLength(cent,True)
#     approx=cv2.approxPolyDP(cent,epsilon,True)
#     res_=cv2.drawContours(img,[approx],-1,(0,0,255),3)
#     print()
#     if len(approx)==4:
#         x, y, w, h = cv2.boundingRect(cent)
#         # print(f"w:{w},h:{h}")
#         if w > 20:
#             i = cv2.rectangle(img3, (x, y), (x + w, y + h), (0, 0, 255), 2)









cv2.imshow("1",img)
cv2.waitKey()
cv2.destroyAllWindows()