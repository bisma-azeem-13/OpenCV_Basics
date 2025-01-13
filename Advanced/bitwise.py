import cv2 as cv
import numpy as np 
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#img = cv.imread("Images\\18.jpg")
#imgr = rescaleFrame(img,scale=0.1)
#cv.imshow("BGR", imgr)

blank = np.zeros((400,400), dtype='uint8')

rect = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
cv.imshow("Rectangle", rect)
cv.imshow("Circle", circle)

#we are going to work with these 2 imgs
#AND - rets only intersecting regions of each other
bw_and = cv.bitwise_and(rect, circle)
cv.imshow("AND", bw_and)

#OR - rets both intersecting and non-intersecting regions of each other
bw_or = cv.bitwise_or(rect, circle)
cv.imshow("OR", bw_or)

#XOR - rets non-intersecting regions of each other
bw_xor = cv.bitwise_xor(rect, circle)
cv.imshow("XOR", bw_xor)

#NOT- inverts color
bw_not = cv.bitwise_not(rect)
cv.imshow("AND", bw_not)
cv.waitKey(0)