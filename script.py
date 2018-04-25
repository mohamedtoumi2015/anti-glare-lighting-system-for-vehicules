import numpy as np
import cv2
from imutils import contours
from matplotlib import pyplot as plt
import imutils




cap = cv2.VideoCapture('night.MP4')

greenUpper = (0, 0, 250)
greenLower = (0, 0, 255)
counter = 0
(dX, dY) = (0, 0)
direction = ""

while(True):
   
    ret, frame = cap.read()

    
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,op = cv2.threshold(gray.copy(),245,255,cv2.THRESH_BINARY)
    op= cv2.erode(op, None, iterations = 2 )
    op = cv2.dilate(op, None, iterations = 4)
    
    
    ROI_frame = frame[500:800, 0:1400]
    ROI = op[500:800, 0:1400]
    ROI_frame = cv2.line(ROI_frame,(154,0),(154,511),(0,0,255),3)
    ROI_frame = cv2.line(ROI_frame,(306,0),(306,511),(0,0,255),3)
    ROI_frame = cv2.line(ROI_frame,(460,0),(460,511),(0,0,255),3)
    ROI_frame = cv2.line(ROI_frame,(614,0),(614,511),(0,0,255),3)
    ROI_frame = cv2.line(ROI_frame,(768,0),(768,511),(0,0,255),3)
    ROI_frame = cv2.line(ROI_frame,(923,0),(923,511),(0,0,255),3)
    ROI_frame = cv2.line(ROI_frame,(1077,0),(1077,511),(0,0,255),3)
    ROI_frame = cv2.line(ROI_frame,(1231,0),(1231,511),(0,0,255),3)
    ROI_frame = cv2.line(ROI_frame,(1385,0),(1385,511),(0,0,255),3)
    #ROI_frame = cv2.line(ROI_frame,(1267,0),(1267,511),(0,0,255),3)
    #for i in range(100):
    #    for j in range(300):
    #        ROI_frame[j,i]=[0,0,255]
    overlay = ROI_frame.copy()
    output = ROI_frame.copy()
    
    cnts = cv2.findContours(ROI.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)[-2]
    print("[INFO] {} unique contours found".format(len(cnts)))
    if len(cnts) > 1 :
        for (i, c) in enumerate(cnts):
            # draw the contour

            ((x, y), r) = cv2.minEnclosingCircle(c)
            if (r>13) :
                if x in range(1,154):
                    cv2.rectangle(overlay, (0, 0), (154, 511),
                        (0, 220, 0), -1)
                    cv2.addWeighted(overlay, 0.3, ROI_frame, 0.9,
                	0, ROI_frame)    
                elif x in range(155,306):
                    cv2.rectangle(overlay, (155, 0), (306, 511),
                        (0, 220, 0), -1)
                    cv2.addWeighted(overlay, 0.3, ROI_frame, 0.9,
                	0, ROI_frame)    
                elif x in range(307,614):
                    cv2.rectangle(overlay, (307, 0), (614, 511),
                        (0, 220, 0), -1)
                    cv2.addWeighted(overlay, 0.3, ROI_frame, 0.9,
                	0, ROI_frame)    
                elif x in range(615,768):
                    cv2.rectangle(overlay, (615, 0), (768, 511),
                        (0, 220, 0), -1)
                    cv2.addWeighted(overlay, 0.3, ROI_frame, 0.9,
                	0, ROI_frame)    
                elif x in range(769,923):
                    cv2.rectangle(overlay, (769, 0), (923, 511),
                        (0, 220, 0), -1)
                    cv2.addWeighted(overlay, 0.3, ROI_frame, 0.9,
                	0, ROI_frame)    
                elif x in range(924,1077):
                    cv2.rectangle(overlay, (924, 0), (1077, 511),
                        (0, 220, 0), -1)
                    cv2.addWeighted(overlay, 0.3, ROI_frame, 0.9,
                	0, ROI_frame)    
                elif x in range(1078,1231):
                    cv2.rectangle(overlay, (1077, 0), (1231, 511),
                        (0, 220, 0), -1)
                    cv2.addWeighted(overlay, 0.3, ROI_frame, 0.9,
                	0, ROI_frame)    
                elif x in range(1232,1385):
                    cv2.rectangle(overlay, (1231, 0), (1385, 511),
                        (0, 220, 0), -1)
                    cv2.addWeighted(overlay, 0.3, ROI_frame, 0.9,
                	0, ROI_frame)    
.                elif x in range(1386,1450):
                    cv2.rectangle(overlay, (1386, 0), (1450, 511),
                        (0, 220, 0), -1)
                    cv2.addWeighted(overlay, 0.3, ROI_frame, 0.9,
                	0, ROI_frame)    
                else:
                    None;
                cv2.putText(ROI_frame, "#{}".format(i + 1), (int(x) - 10, int(y)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                cv2.drawContours(ROI_frame, [c], -1, (0, 255, 0), 2)
                
    
    cv2.imshow('frame',ROI)
    cv2.imshow('final',ROI_frame)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
