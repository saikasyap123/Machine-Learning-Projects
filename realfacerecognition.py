import cv2
import numpy as np
import os 
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('traineddata.yml')
cascade = cv2.CascadeClassifier('D:\haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
while True:
    ret, img =cam.read()
    #img = cv2.flip(img, -1) # Flip vertically
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = cascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5
       )
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
    if id==1 and confidence<75:
        
            cv2.putText(
                    img, 
                    'user'+str(confidence), 
                    (x+5,y-5), 
                    cv2.FONT_HERSHEY_COMPLEX,
                    1, 
                    (255,255,255), 
                    2
                   )
    else:
             cv2.putText(
                    img, 
                    'unknown'+str(confidence), 
                    (x+5,y-5), 
                    cv2.FONT_HERSHEY_COMPLEX,
                    1, 
                    (255,255,255), 
                    2
                   )
    cv2.imshow("image",img)
    if cv2.waitKey(1)==13:
        braek
cam.release()
cv2.destroyAllWindows()
