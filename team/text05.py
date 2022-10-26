import cv2
import numpy as np

img=cv2.imread("./train-5/184/184.jpg")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template=cv2.imread("./train-5/184/184_1.jpg",0)
# h,w=template.shape[:2]
res=cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)#模板匹配
threshold=0.8
loc=np.where(res>=threshold)
for pt in zip(*loc[::-1]):
    bottom_right=(pt[0]+40,pt[1]+40)
    cv2.rectangle(img,pt,bottom_right,(0,0,255),2)
cv2.imshow("r",img)
cv2.waitKey()
cv2.destroyAllWindows()
# min_val,max_val,min_loc,max_val=cv2.minMaxLoc(res)
# top_left=min_loc
# bottom_right=(top_left[0]+w,top_left[1]+h)
# cv2.rectangle(img,top_left,bottom_right,255,2)