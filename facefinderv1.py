import cv2
import os
import time
import numpy as np


cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')


while(cap.isOpened()):
    #Capture the video by the frame
    ret, frame = cap.read()
    #Convert the video into grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #detect faces and scalefactor for capturing image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors = 8)
    for (x, y, w, h) in faces:
        #Region of interest
        roi_gray = gray[y:y+h, x:x+w] #(ycord start, ycord end) same with x cord 
        roi_color = frame[y:y+h, x:x+w]
        #Create new image
        img_item = "new_image.png"
        #Create image
        cv2.imwrite(img_item, roi_gray)

        #Create color
        color = (255, 0, 0)
        stroke = 2
        end_cordinate_x = x + h
        end_cordinate_y = y + h
        #draw rectangle onto the face 
        cv2.rectangle(frame, (x,y), (end_cordinate_x, end_cordinate_y), color, stroke)
        print('Number of faces found: ', len(faces))

        eyes = eye_cascade.detectMultiScale(roi_gray)    
        for (ex, ey, ew, eh) in eyes:
            eye_detect = cv2.rectangle(roi_color,(ex,ey), (ex+ew,ey+eh), (255,0,255), 2)

    #Display the frame
    cv2.imshow('Face', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break