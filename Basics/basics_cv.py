import cv2 as cv
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)




img = cv.imread("Images\\15.jpg")
resized_img = rescaleFrame(img,scale=0.1)
cv.imshow("BGR", resized_img)

#converting img to grayscale
gray = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY) # image and what color you want to convert in
cv.imshow("Gray", gray)

#Blur - bluring an img remove some of noise that exists in the image
#Gaussian Blur
#src img, kernel size(2x2 tuple-window size that ocv use to compute blow on img, odd num)-increase blur by increasing kernel size
blur = cv.GaussianBlur(resized_img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

#Edge Cascade - edges present in the img - like lined vector of img
canny = cv.Canny(resized_img, 125, 175) # src and 2 threshold values
cv.imshow("Canny", canny)

#Dilating img - by using some structure like canny edges
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow("Dialated", dilated)

#Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow("Erdoded", eroded)

#Resize img
resize = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
#inter_area is useful if you are shrinking theimage to dims that are smaller than og dims
#if you want to enlarge img and scale to much larger dims, use Inter_linear or inter_cubic
#cubic is slowest but gives highest quality
cv.imshow("Resized", resize)

# crop img
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)
cv.waitKey(0)