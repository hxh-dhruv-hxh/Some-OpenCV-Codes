import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv-master/samples/data/sudoku.png', cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

# Finding vertical edges
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
# Finding horizontal edges
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

# Combining the sobel x and y filters
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

edges = cv2.Canny(img, 150, 250)

titles = ['image', "lap", 'SobelX', 'SobelY', 'sobelCombined', 'Canny']
images = [img, lap, sobelX, sobelY, sobelCombined, edges]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()