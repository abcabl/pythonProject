import cv2
import numpy as np

img = cv2.imread("./train-5/1308/1308.jpg")
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# kernel=np.ones((10,10),np.uint8)
# oping=cv2.morphologyEx(img1,cv2.MORPH_OPEN,kernel)

a=cv2.GaussianBlur(img1,(15,15),0)



cv2.imshow("1",a)


cv2.waitKey()
cv2.destroyAllWindows()