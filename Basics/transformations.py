import cv2 as cv
import numpy as np 
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread("Images\\15.jpg")
imgr = rescaleFrame(img,scale=0.1)
cv.imshow("Image", imgr)

#Translation - shifting img along x and y axis (up,down,left,right)
#x,y - number of pixels to be shifted
def translate(img,x,y):
    translation_matrix = np.float32([[1,0,x],[0,1,y]]) #takes 2 lists(2Dim)
    dims = (img.shape[1], img.shape[0]) # w , h respectively
    return cv.warpAffine(img, translation_matrix, dims)
#affine transformation includes operations like translation, rotation, scaling, and shearing.
# -x = Shifts left , -y= Up, +y = Down, +x = right
translated = translate(imgr, -100, -100)
cv.imshow("Translated", translated)

#rotation
def rotate(img, angle, rot_point=None):
    (height, width) = img.shape[:2]

    if rot_point is None: #if None means rotate around the center
        rot_point = (width//2, height//2) #midpoints
    
    rot_matrix = cv.getRotationMatrix2D(rot_point, angle, scale=1.0) #keeping scale as its default val
    dims =(width, height)

    return cv.warpAffine(img, rot_matrix, dims)

rotated = rotate(imgr , -70)
cv.imshow("Rotated", rotated)

#flip
flip = cv.flip(imgr,1)#src, flip code(0[vertically],1[horizonally],-1[both])
cv.imshow("Flip", flip)


cv.waitKey(0)

