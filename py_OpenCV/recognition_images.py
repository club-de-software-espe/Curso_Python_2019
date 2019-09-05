from cv2 import *

face_cascade = CascadeClassifier('haarcascade_frontalface_default.xml')
image = imread('example_images/04_faces.jpg')
gray = cvtColor(image, COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1,10)
# print(faces)
for (x, y, w, h) in faces:
    rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 1)
    # putText(image, 'Face', (x,y+h+12), 0, 0.4, (0,0,0),1)
imshow('Image', image)
waitKey(0)