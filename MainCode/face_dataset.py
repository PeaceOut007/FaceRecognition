import cv2 as cv
import os

def createNames_list(labels, n):
    for i in range(0,n):
        name = input('Enter the name of the person:')
        labels.append(name)

    return labels

n = int(input('Enter the number of people you want to add to the database:'))
labels = []

createNames_list(labels, n)

with open(r'C:/Users/KIIT/Desktop/Codes/AttendanceSystem-main/MainCode/name_list.txt', 'w') as fp:
    for item in labels:
        fp.write("%s\n" % item)

os.chdir('C:/Users/KIIT/Desktop/Codes/AttendanceSystem-main/Dataset')

for label in labels:
    if not os.path.exists(label):
        os.mkdir(label)

camera = cv.VideoCapture(0)

for folder in labels:
    count = 0
    print("Press 's' to start data collection for "+folder)
    userinput = input()
    if userinput != 's':
        print("Wrong Input..........")
        exit()

    while count<100:
        status, frame = camera.read()

        if not status:
            print("Frame is not been captured..Exiting...")
            break
        cv.imshow("Video Window",frame)

        cv.imwrite('C:/Users/KIIT/Desktop/Codes/AttendanceSystem-main/Dataset/'+folder+'/img'+str(count)+'.png',frame)

        count=count+1
        if cv.waitKey(1) == ord('q'):
            break

camera.release()
cv.destroyAllWindows()