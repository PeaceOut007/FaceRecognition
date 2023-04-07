import cv2

cam = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print('failed to grab frame')
        break
    cv2.imshow('test', frame)
    k  = cv2.waitKey(1)
    # if the escape key is been pressed, the app will stop
    if k%256 == 27:
        print('escape hit, closing the app')
        break
    # if the spacebar key is been pressed screenshots will be taken
    elif k%256  == 32:
        cv2.imwrite('C:/Users/KIIT/Desktop/Codes/AttendanceSystem-main/Check/img.png',frame)
        count += 1

cam.release()
cv2.destoryAllWindows()