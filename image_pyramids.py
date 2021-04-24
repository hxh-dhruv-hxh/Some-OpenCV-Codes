import cv2
import numpy as np

# img = cv2.imread('opencv-master/samples/data/lena.jpg')
#
# upr = cv2.pyrUp(img)
# down = cv2.pyrDown(img)
#
# cv2.imshow('image', img)
# cv2.imshow('upScaled', upr)
# cv2.imshow('Down Scaled', down)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# LaPlacian Pyramid

img = cv2.imread('opencv-master/samples/data/lena.jpg')
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i), layer)

layer = gp[5]
cv2.imshow('Upper Level Gaussian Pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussian_extend = cv2.pyrUp(gp[i])
    LaPlacian = cv2.subtract(gp[i-1], gaussian_extend)
    cv2.imshow(str(i), LaPlacian)

cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()













