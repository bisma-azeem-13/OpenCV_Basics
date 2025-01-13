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

gray = cv.cvtColor(imgr, cv.COLOR_BGR2GRAY)
cv.imshow("GRAY", gray)

#1. Simple Thresholding: manually specify a specific thresh val
#passing gray is must
threshold , thresh = cv.threshold(gray, 100 ,255, cv.THRESH_BINARY )
cv.imshow("Simple Thresh", thresh)

threshold , thresh_inv = cv.threshold(gray, 100 ,255, cv.THRESH_BINARY_INV )
cv.imshow("Simple Thresh Inverse", thresh)

#2. Adaptive Thresh- let the comp find optimal thresh value , blockSize =neighborhood  kernel size, C - finetune thresh val
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11,  3)
cv.imshow("Adaptive Thresh", adaptive_thresh)

cv.waitKey(0)