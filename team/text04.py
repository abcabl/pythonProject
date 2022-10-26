import cv2
import numpy as np

img = cv2.imread("./train-5/184/184.jpg")
# kernel=np.ones((3,3),np.uint8)
# erosion=cv2.erode(img,kernel,iterations=3)#腐蚀

# l=erosion
l=img
gray= cv2.cvtColor(l, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,60, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for cnt in contours:#边缘检测
    x,y,w,h=cv2.boundingRect(cnt)
    print(f"w:{w},h:{h}")
    if 70>w>20:
        i=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)

cv2.imshow("11",img)





#cv2.imshow("r",img)
cv2.waitKey()
cv2.destroyAllWindows()