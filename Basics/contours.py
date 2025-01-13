import cv2 as cv
import numpy as np 
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread("DFD\\22.jpeg")
imgr = rescaleFrame(img,scale=0.1)
cv.imshow("Image", img)

blank =np.zeros(img.shape, dtype='uint8')
cv.imshow("Blank", blank)

#How to idfy contours: 
#Contours are basically boundaries of objs, the live/curve of continuous pts along the boundary of an obj
#from math pov: they are not same as imgs - both are two dif things. 
#contours are useful in shape analysis, obj detection and face recognition

# 1. chg img to grayscale
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow("Image Gray", gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)
#2. taking edges of the img
canny = cv.Canny(blur, 125,175)
cv.imshow("Canny", canny)

#by using thresholding teq - tries to binarize the img (B&W)
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) #src, minthrsh, maxval, type of thresh
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.imshow("Thresh", thresh)
#viz contours of img  by drawing on blank img
cv.drawContours(blank, contours, contourIdx=-1, color=(0,0,255), thickness=1)
cv.imshow("Contours Drawn on Img", blank)
print(f'{len(contours)} contours found.')


#3. finding contours via contour func , rets countours and hierarchies
#takes src, mode in which you want to find contour(many other options) and cont approx method(many other options)
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#countours is py list of all coords of contours that were find in img
#hierarchy is hiercal rep of contours
print(f'{len(contours)} contours found.')


cv.waitKey(0)