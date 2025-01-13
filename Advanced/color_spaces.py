import cv2 as cv
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)




img = cv.imread("Images\\14.jpg")
imgr = rescaleFrame(img,scale=0.1)
cv.imshow("BGR", imgr)

#converting BGR to grayscale
gray = cv.cvtColor(imgr, cv.COLOR_BGR2GRAY) # image and what color you want to convert in
cv.imshow("Gray", gray)

#RBG to HVS (Hue Saturation Value)
hsv = cv.cvtColor(imgr, cv.COLOR_BGR2HSV) # image and what color you want to convert in
cv.imshow("HSV", hsv)
#BGR to LAB
lab = cv.cvtColor(imgr, cv.COLOR_BGR2LAB) # image and what color you want to convert in
cv.imshow("LAB", lab)
#BGR2RGB
rgb = cv.cvtColor(imgr, cv.COLOR_BGR2RGB) # image and what color you want to convert in
cv.imshow("RGB", rgb)


cv.waitKey(0)