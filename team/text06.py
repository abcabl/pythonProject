import cv2
import numpy as np
from fontTools.misc import vector
from numpy import poly

img = cv2.imread("./train-5/1308/1308.jpg")
img2 = cv2.imread("./train-5/1308/1308.jpg",0)

img3=cv2.imread("./train-5/1308/1308.jpg")

ret, thresh = cv2.threshold(img2,80, 255, cv2.THRESH_BINARY)


kernel=np.ones((4,4),np.uint8)

erosion=cv2.erode(thresh,kernel,iterations=3)#腐蚀
dilate=cv2.dilate(erosion,kernel,iterations=1)#膨胀



ret1, thresh1 = cv2.threshold(dilate,80, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow("er",erosion)
# cv2.imshow("yuan",img)
cv2.imshow("yuan",thresh1)



contours, hierarchy = cv2.findContours(thresh1 , cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

draw=thresh1.copy()
# res=cv2.drawContours(img,contours,-1,(0,255,0),2)






for cent in contours:
    epsilon=0.001*cv2.arcLength(cent,True)
    approx=cv2.approxPolyDP(cent,epsilon,True)
    res_=cv2.drawContours(img,[approx],-1,(0,0,255),2)
    print()#上线70
    if len(approx)>30:
        x, y, w, h = cv2.boundingRect(cent)
        # print(f"w:{w},h:{h}")
        # if w > 30 :
        i = cv2.rectangle(img3, (x, y), (x + w, y + h), (0, 0, 255), 2)





cv2.imshow("1",img)
cv2.imshow("2",img3)









cv2.waitKey()
cv2.destroyAllWindows()

