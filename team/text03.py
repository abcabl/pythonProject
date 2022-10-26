import cv2

img = cv2.imread("./train-5/184/184.jpg")


l=img
for i in range(30):
    up=cv2.pyrUp(l)
    up=cv2.pyrDown(up)
    l=img-up
cv2.imshow("r",l)#金字塔处理

# gray= cv2.cvtColor(l, cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(gray,80, 255, cv2.THRESH_BINARY)#二值
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# # draw = img.copy()
# # res = cv2.drawContours(draw, contours, -1, (0, 255, 0), 2)
# # cv2.imshow("r", res)
# for cnt in contours:#边缘检测
#     x,y,w,h=cv2.boundingRect(cnt)
#     print(f"w:{w},h:{h}")
#     # if 40>w>10:
#     i=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)


# cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()
