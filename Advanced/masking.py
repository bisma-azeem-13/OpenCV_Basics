import cv2 as cv
import numpy as np 
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread("Images\\15.jpg")
imgr = rescaleFrame(img,scale=0.1)
cv.imshow("BGR", imgr)

#1. Create blank
blank = np.zeros(imgr.shape[:2], dtype='uint8') #size/dim of blank should be same as og img
cv.imshow("Blank", blank)

#2. Create Mask by drawing circle on blank img
mask = cv.circle(blank, (imgr.shape[1]//2, imgr.shape[0]//2), 200, 255, -1)
cv.imshow("Mask", mask)

#3. masked img
masked_img = cv.bitwise_and(imgr,imgr, mask = mask) #src, src , mask we created
cv.imshow("Masked Img", masked_img)

cv.waitKey(0)