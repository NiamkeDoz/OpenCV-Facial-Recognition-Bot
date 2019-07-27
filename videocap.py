#Working with video 


import cv2
import numpy as np
import datetime

#capture video from webcam
cap = cv2.VideoCapture(0)



#while loop to continuously capture frame
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #Get the current date and time
    currtime = str(datetime.datetime.now())

    # Our operations on the frame come here
    
    #Load font
    font = cv2.FONT_HERSHEY_SIMPLEX

    #Places text on to video 
    frame = cv2.putText(frame, currtime, (800, 650), font, 1, (255,0,0), 1, cv2.LINE_AA)
   
    # Display the resulting frame
    cv2.imshow('Facial Recognition', frame)
    if cv2.waitKey(200) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()