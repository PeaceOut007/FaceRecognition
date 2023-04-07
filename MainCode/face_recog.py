import cv2 as cv

DIR = r'C:/Users/KIIT/Desktop/Codes/AttendanceSystem-main/MainCode'

people = []

with open(r'C:/Users/KIIT/Desktop/Codes/AttendanceSystem-main/MainCode/name_list.txt', 'r') as fp:
    for line in fp:
        x = line[:-1]
        people.append(x)

haar_cascade = cv.CascadeClassifier('C:/Users/KIIT/Desktop/Codes/AttendanceSystem-main/MainCode/haar_face.xml')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('C:/Users/KIIT/Desktop/Codes/AttendanceSystem-main/MainCode/face_trainer.yml')

img = cv.imread('C:/Users/KIIT/Desktop/Codes/AttendanceSystem-main/Check/img.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# detect face in the image
face_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 4)
for (x,y,w,h) in face_rect:
    faces_roi = gray[y:y+h, x: x+h]

    label,confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX,1.0, (0,255,0), thickness = 2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness = 1)

cv.imshow('Detected Face', img)
cv.waitKey(0)