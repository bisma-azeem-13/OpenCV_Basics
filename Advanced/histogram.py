import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np 

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread("Images\\11.jpg")
imgr = rescaleFrame(img,scale=0.1)
cv.imshow("BGR", imgr)

#Hist for Grayscale imgs
#1. Convert to grayscale
gray = cv.cvtColor(imgr, cv.COLOR_BGR2GRAY)
cv.imshow("GRAY", gray)

#4. create mask and do hist of that particular masked area
blank = np.zeros(imgr.shape[:2], dtype='uint8')

mask = cv.circle(blank, (imgr.shape[1]//2, imgr.shape[0]//2), 100, 255, -1)
cv.imshow("Mask", mask)

masked = cv.bitwise_and(gray, gray, mask = mask) #src, src , mask we created
cv.imshow("Masked Img", masked)

#2. Calculate Hist
#need to pass list of imgs, num of channels / index of channel to comp hist , Mask, HistSize = # of Bins, range of all possible pixel values
#gray_hist = cv.calcHist([gray],[0],mask,[256] , [0,256]) 

#3. Draw Graph
#plt.figure()
#plt.title("Grayscale Histogram")
#plt.xlabel("Bins")
#plt.ylabel("num of pixels")
#plt.plot(gray_hist)
#plt.xlim([0,256])
#plt.show()

#ColorHist
masked = cv.bitwise_and(imgr, imgr, mask = mask) #src, src , mask we created
cv.imshow("Masked Img", masked)

plt.figure()
plt.title("COlor Histogram")
plt.xlabel("Bins")
plt.ylabel("num of pixels")



colors =('b', 'g', 'r')
for i, col in enumerate(colors):
    hist=cv.calcHist([imgr],[i], mask, [256],[0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])

plt.show()
cv.waitKey(0)