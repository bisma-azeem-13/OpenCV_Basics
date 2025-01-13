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

#spliting the img into respective colors
b,g,r = cv.split(imgr)
#displaying
cv.imshow("Blue",b)
cv.imshow("Green",g)
cv.imshow("Red",r)

#viz the shapes of img
print(imgr.shape)
print(r.shape)
print(g.shape)
print(b.shape)

#merging individuals
merged = cv.merge([b,g,r])
cv.imshow("Merged",merged)

#now all these imgs are grayscale imgs and the intensity tells their color
#displaying actual colors of channel on img by reconstructing img on blank

blank = np.zeros(imgr.shape[:2], dtype='uint8')

blue= cv.merge([b,blank,blank])
green= cv.merge([blank,g,blank])
red= cv.merge([blank,blank,r])

cv.imshow("Blue",blue)
cv.imshow("Green",green)
cv.imshow("Red",red)

cv.waitKey(0)