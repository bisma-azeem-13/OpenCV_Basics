import cv2 as cv
def rescaleFrame(frame, scale=0.99):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread("Images\\19.jpg")
imgr = rescaleFrame(img,scale=0.1)
#cv.imshow("BGR", imgr)

#1. Convert img into grayscale
gray = cv.cvtColor(imgr, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#2. Reading haar_face.xml file

haar_cascade = cv.CascadeClassifier("haar_face.xml")

#3. Face detection
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1 , minNeighbors=5) # src img, scale factor, min_neighbors
#this func will return the rectangular coordinates of detected img
#printing number of faces detected, by printing len of facase_rect var
print(f'Number of faces found = {len(faces_rect)}')

#4. drawing cords found by classifier on the detected face s
# by look over the faces_rect list and grabbing those coords

for (x,y,w,h) in faces_rect:
    cv.rectangle(imgr, (x,y), (x+w,y+h), (0,255,0), thickness=2) #src, cord1, cord2, color

cv.imshow("Detected Faces,", imgr)

#On a group, it detects faces wrong, fix that by fine tuning scalefactor and minneighbours
#Still it dosent work the best. Use Dlibs instead in projects
cv.waitKey(0)