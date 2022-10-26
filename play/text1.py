import cv2 as cv

def face_detect_demo():
        gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        face_detector=cv.CascadeClassifier('D:\\opencv\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml')
        faces=face_detector.detectMultiScale(gray)
        for x,y,w,h in faces:
            cv.rectangle(img,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)
            cv.imshow("aaa",img)




img=cv.imread('5d3e0ebd146eb6db144fbe09180a1c4d23842cdd_raw.jpg')
face_detect_demo()

cv.waitKey(0)
cv.destroyAllWindows()