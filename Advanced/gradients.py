import cv2 as cv
import numpy as np 
def rescaleFrame(frame, scale=0.99):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread("Images\\11.jpg")
imgr = rescaleFrame(img,scale=0.1)
cv.imshow("BGR", imgr)

gray = cv.cvtColor(imgr, cv.COLOR_BGR2GRAY)
cv.imshow("GRAY", gray)

# laplacian
lap = cv.Laplacian(gray, cv.CV_64F) #src , ddepth / data depth
lap = np.uint8(np.absolute(lap)) #convert the Lap output into format suitable for displaying as an image.
#After taking the absolute values, the data is still in a floating-point format (cv.CV_64F).
# np.uint8(...) converts the floating-point values, to 8-bit unsigned integers (range: 0 to 255), 
# which is the standard format for grayscale images in OpenCV.
cv.imshow("laplacian", lap)

#sobel
sobelx= cv.Sobel(gray, cv.CV_64F, 1, 0) # set dir of x=1 and y=0
sobely= cv.Sobel(gray, cv.CV_64F, 0, 1) # set dir of x=0 and y=1
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)
cv.imshow("Sobel Combined", combined_sobel)

#canny
canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)
cv.waitKey(0)