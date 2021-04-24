import numpy as np
import cv2

cap = cv2.VideoCapture('opencv-master/samples/data/vtest.avi')

# fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
fgbg = cv2.createBackgroundSubtractorKNN()

while True:

    ret, frame = cap.read()

    if frame is None:
        break

    fgmask = fgbg.apply(frame)

    cv2.imshow('Frame', frame)
    cv2.imshow('MG MASK Frame', fgmask)

    if cv2.waitKey(30) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()

