import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    #Capture the video by the frame
    ret, frame = cap.read()
    #Convert the video into grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #detect faces and scalefactor for capturing image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors = 8)
    for (x, y, w, h) in faces:
        print(x, y, w, h)
        #Region of interest 
        roi_gray = gray[y:y+h, x:x+w] #(ycord start, ycord end) same with x cord 
        roi_color = frame[y:y+h, x:x+w]
        #Create new image
        img_item = "new_image.png"
        cv2.imwrite(img_item, roi_gray)

        #Create color
        color = (255, 0, 0)
        stroke = 2
        end_cordinate_x = x + h
        end_cordinate_y = y + h
        #draw rectangle onto the face 
        cv2.rectangle(frame, (x,y), (end_cordinate_x, end_cordinate_y), color, stroke)
    #Display the frame
    cv2.imshow('Face', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

#when the application closes, release all the resources
cap.release()
cv2.destroyAllWindows()