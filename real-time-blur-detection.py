#This program can tell when the real-time video stream is blur and when it is clear. #

import cv2
import numpy as np

source = cv2.VideoCapture(0)			#to capture video stream from camera

font = cv2.FONT_HERSHEY_SIMPLEX 

while(source.isOpened()):
	# Load the image and convert it to grayscale
	ret, image = source.read()
	#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# Calculate the Laplacian variance
	laplacian = cv2.Laplacian(image, cv2.CV_64F)
	#variance = cv2.meanStdDev(laplacian)[1]**2
	variance = laplacian.var()

	# Define the threshold value
	threshold = 50

	# Compare the variance with the threshold
	if variance < threshold:
		cv2.putText(image,'Blur!!!', (50, 50), font, 1, (255,0, 0), 2)
		
		filtered_frame = cv2.GaussianBlur(image, (5, 5), 0)
    
    		#cv2.imshow('Frame', frame)

	else:
		cv2.putText(image,'Sharp Image', (50, 50), font, 1, (255,0, 0), 2) 
		filtered_frame = image

	    # displaying the video
	cv2.imshow("Live", image)

	# exiting the loop
	key = cv2.waitKey(5)
	if key == ord("q"):
		break
      
# closing the window
cv2.destroyAllWindows()
source.release()
