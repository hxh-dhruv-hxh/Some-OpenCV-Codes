import cv2
import numpy as np

def click_event(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ", ", y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x)+ ', ' + str(y)
        cv2.putText(img2, strXY, (x, y), font, 0.5, (255, 255, 255), 2)
        cv2.imshow('img2', img2)

img1 = cv2.imread('image_1.png')
#print(img1.shape)
img2 = np.zeros((341, 512, 3), np.uint8)
img2 = cv2.rectangle(img2, (183, 6), (304, 110), (255, 255, 255), -1)

bitXor = cv2.bitwise_xor(img1, img2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('xor', bitXor)
#cv2.setMouseCallback('img2', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()