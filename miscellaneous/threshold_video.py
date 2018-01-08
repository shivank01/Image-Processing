import cv2
import numpy as np

cap=cv2.VideoCapture(0)
fourc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourc, 20.0, (640,480))

while(True):
	ret,frame=cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	gaus=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
	cv2.imshow('frame',frame)
	
	cv2.imshow('gaus',gaus)
	out.write(gaus)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
out.release()
cv2.destroyAllWindows()