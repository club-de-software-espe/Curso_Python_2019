from cv2 import *
import numpy as np

image = imread('example_images/01_face.jpg', 0)
image=resize(image, (500, 500))
# image=np.zeros((500,500), np.uint8)
line(image, (0,0), (500, 500), (0,0,255), 2) # P0, PF, Color, Thinkness
arrowedLine(image, (0,500), (400, 20), (255,0,0), 2)
rectangle(image, (40,40), (460,460), (0,255,0),1)
circle(image, (250,250), 100, (30,50,90), 4)
putText(image, 'Curso Python', (40,100), FONT_HERSHEY_COMPLEX_SMALL, 2, (80,20,106),1)
imshow('Image', image)
waitKey(0)
destroyAllWindows()
imwrite('output_images/out1.jpg',image)
