import cv2

img = cv2.imread('opencv-master/samples/data/lena.jpg', flags=0)

cv2.imshow('B/W', img)
k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()

elif k == ord('s'):
    # Writing the read image into our disk
    cv2.imwrite('lena_copy.jpg', img)
    cv2.destroyAllWindows()
