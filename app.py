import cv2
import csv
from datetime import datetime
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
file = open('attendance.csv', 'a', newline='')
writer = csv.writer(file)
marked_names = set()
name = input("Enter your name: ")
print("Press 'q' to exit")
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        name = "User"
        if name not in marked_names:
            time = datetime.now().strftime('%H:%M:%S')
            writer.writerow([name, time])
            marked_names.add(name)
            print(f"{name} marked at {time}")
    cv2.imshow('Face Attendance System', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
file.close()
cv2.destroyAllWindows()