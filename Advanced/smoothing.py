import cv2 as cv
import numpy as np 
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread("Images\\18.jpg")
imgr = rescaleFrame(img,scale=0.1)
cv.imshow("BGR", imgr)

#Blurring Teqs
#Averaging - by evg the pixels around given kernel size
avg = cv.blur(imgr,(3,3))
cv.imshow("Blur", avg)

#gausblur - less but natural blur 
gauss = cv.GaussianBlur(imgr,(3,3),0) #std dev
cv.imshow("GBlur", gauss)

#median blur - finds median of pixels and reduces more noise - like painting
med = cv.medianBlur(imgr,3)
cv.imshow("Median", med)

#Bilateral
bil = cv.bilateralFilter(imgr, 10, 35,25) # 5 is diameter
cv.imshow("Bil", bil)
cv.waitKey(0)