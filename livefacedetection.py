import cv2
import numpy as np 
fc = cv2.CascadeClassifier('D:\haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = fc.detectMultiScale(gray,1.32,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(frame,"face found",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),5)
    cv2.imshow("image",frame)
   
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
cam.release()
cv2.destroyAllWindows