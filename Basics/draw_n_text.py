import cv2 
import numpy as np 

#creating blank pg to draw on
blank = np.zeros((500,500,3), dtype='uint8') #unit8 is img , 3 is color channel
#displaying blank img
cv2.imshow("Blank", blank)

#1. Paint img a certain color
#painting whole img green
blank[:]= 0,255,0 
#color certain portion
blank[200:300, 300:400 ] = 255,0,0
blank[100:150, 150:200 ] = 0,0,255
cv2.imshow("Colored", blank)
#2. Draw rectangle 
cv2.rectangle(blank,(0,0),(250,500),(255,0,0), thickness=cv2.FILLED) #img,origin, endpoint, color, fill the rect or write -1 in thinkness
cv2.imshow("Rectangle", blank)
#3.Draw a circle
cv2.circle (blank, (250,250), 150, (0,0,255), thickness=-1)# img, midpoind, radius, color, thinkness
cv2.imshow("Circle", blank)
#4. Draw a standalone line
cv2.line(blank, (110,110),(250,500),(0,0,0), thickness=3)
cv2.imshow("Line", blank)

#text on img
cv2.putText(blank, "Hello", (225,255), cv2.FONT_HERSHEY_COMPLEX, fontScale=1.0, color=(0,255,255), thickness=3)
cv2.imshow('Text',blank)
#img = cv2.imread('Images//13.jpg')
#cv2.imshow('Image', img)
cv2.waitKey(0)