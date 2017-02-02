import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import cv2
import numpy as np

cap = cv2.VideoCapture("lcw.mp4")

while cap.isOpened():
    
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_white = np.array( [70,0,100] )
    upper_white = np.array( [185,185,255] )
    # mask either 0 (false) or 1 (true)
    mask = cv2.inRange( hsv, lower_white, upper_white )
    # every match
    res = cv2.bitwise_and( frame, frame, mask=mask )

    cv2.imshow('res',res)

    cv2.waitKey(100)

cap.release()
cv2.destroyAllWindows()

# track feet instead?
