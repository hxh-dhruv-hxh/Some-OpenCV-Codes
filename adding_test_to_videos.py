import datetime
import cv2

cap = cv2.VideoCapture('opencv-master/samples/data/Megamind.avi')

# We can use 3 in cv2.get() for cv2.CAP_PROP_FRAME_WIDTH
# We can use 4 in cv2.get() for cv2.CAP_PROP_FRAME HEIGHT

while (cap.isOpened()):

    ret, frame = cap.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(datetime.datetime.now())
        frame = cv2.putText(frame, text, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('MegaMind',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
