import numpy as np
import cv2 as cv

def nothing(x):
    print(x)

# Creating a black image using numpy
img = np.zeros((300, 512, 3), np.uint8)

# Creating a named window so that we can add different windows into it
cv.namedWindow('image')

cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)

switch = '0: OFF\n 1: ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while True:
    cv.imshow('image', img)
    if cv.waitKey(1) & 0xFF == 27:
        break

    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0

    else:
        img[:] = [b, g, r]

cv.destroyAllWindows()











