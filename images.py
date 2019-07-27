#How to add images and draw shapes on those images!

import cv2
import numpy as np

#Load colored image
img = cv2.imread('images/will01.jpg', 0)
#img2 = cv2.imread('images/will01.jpg', 1)


#How to draw images using numpy
#img2 = np.zeros([512, 512,3], np.uint8)

##draw a line onto image
#img2 = cv2.line(img2, (0,0), (255, 255), (147, 96, 44), 10)

###draw arrowed line on image
#img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 10)

#Draw a rectangle
img = cv2.rectangle(img, (384, 0), (300, 128), (0,0,255), 10)

#Draw a circle
img = cv2.circle(img, (250, 63), 63, (255,0,0), 10)

#Load in a font
font = cv2.FONT_HERSHEY_SIMPLEX
#Display text onto image 
img2 = cv2.putText(img2, 'OpenCV Text Test', (320,458), font, 0.5, (0,0,0), 1, cv2.LINE_AA)


#display images
#cv2.imshow('image', img)
cv2.imshow('image2', img2)

#how to 
while(True):

    #Press q to quit
    if cv2.waitKey(200) & 0xFF == ord('q'):
        break

#destroys windows when application is done
cv2.destroyAllWindows()