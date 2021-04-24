import numpy as np
import cv2

img = cv2.imread('opencv-master/samples/data/pic1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.40, 10)

corners = np.uint64(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, (255, 0, 0), -1)

cv2.imshow('dst', img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

