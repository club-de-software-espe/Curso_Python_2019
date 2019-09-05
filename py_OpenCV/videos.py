import numpy as np
from cv2 import *

cap = VideoCapture(0)
fourcc = VideoWriter_fourcc(*'XVID')
out = VideoWriter('output_videos/output.avi',fourcc, 20, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        #frame = flip(frame,1)
        #cv2.arrowedLine(frame, (0,500), (400, 20), (255,0,0), 2)
        # write the flipped frame
        out.write(frame)
        imshow('Video',frame)
        if waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
destroyAllWindows()