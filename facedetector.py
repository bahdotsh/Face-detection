# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 19:17:29 2017

@author: Gokul
"""

import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
mouth_cascade=cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

capture = cv2.VideoCapture(0)

    
fourcc = cv2.cv.CV_FOURCC(*'XVID') 
   # videoOut = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

while (capture.isOpened()):
    ret, frame = capture.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        mouth=mouth_cascade.detectMultiScale(gray,1.7,11)
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        for(mx,my,mw,mh) in mouth:
            my = int(my - 0.15*mh)
            cv2.rectangle(frame,(mx,my),(mx+mw,my+mh),(0,0,255),2)
            
    if ret:
         # videoOut.write(frame)
         
         cv2.imshow('Video Stream', frame)
    else:
        break
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
        
        
capture.release()
#videoOut.release()
cv2.destroyAllWindows()
 