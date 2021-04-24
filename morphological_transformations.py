import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv-master/samples/data/smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((4, 4), np.uint8)

erosion = cv2.erode(mask, kernal, iterations=1)
dilation = cv2.dilate(erosion, kernal, iterations=2)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
# Morphological gradient is difference between dilation and erosion
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)

# top hat is the difference between the image and opening
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)

titles = ['image', 'mask', 'erosion', 'dilation', 'opening', 'closing', 'mg', 'th']
images = [img, mask, erosion, dilation, erosion, opening, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()