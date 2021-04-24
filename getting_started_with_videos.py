import cv2

cap = cv2.VideoCapture('opencv-master/samples/data/Megamind.avi')
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
out = cv2.VideoWriter('output.avi', fourcc, cap.get(cv2.CAP_PROP_FPS),
                      (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

print(cap.isOpened())

while (cap.isOpened()):

    ret, frame = cap.read()

    if ret == True:

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        out.write(gray)

        cv2.imshow('Megamind',gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
out.release()


