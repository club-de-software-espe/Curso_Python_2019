import numpy as np
from cv2 import *

cap = VideoCapture(0)
face_cascade = CascadeClassifier('haarcascade_frontalface_default.xml')
fourcc = VideoWriter_fourcc(*'XVID')
out = VideoWriter('output_videos/output_recognition.avi',fourcc, 20, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = flip(frame,1)
    if ret:
        gray = cvtColor(frame, COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1,10)
        for (x, y, w, h) in faces:
            rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
            putText(frame, 'Memo', (x,y+h+12), 0, 0.4, (0,0,0),1)
        out.write(frame)

        imshow('Video',frame)
        if waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
destroyAllWindows()