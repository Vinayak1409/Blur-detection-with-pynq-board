# sorting blurred and sharp images through a pile of random photos #
#final submitted code for EEE F348 FPGA-based system design lab #

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Define the directory containing the images
dir_path = "../test_images"
font = cv2.FONT_HERSHEY_SIMPLEX
threshold = 200

# Loop through all files in the directory
for filename in os.listdir(dir_path):
    # Check if the file is an image (JPEG or JPG)
	if filename.endswith(".jpg") or filename.endswith(".jpeg"):
		# Load the image
		img_path = os.path.join(dir_path, filename)
		img = plt.imread(img_path)
		variance = cv2.Laplacian(img, cv2.CV_64F).var()
		
		if variance < threshold:
			cv2.putText(img,'Blur Image', (0, 50), font, 0.5, (255,255, 69), 2)
		else:
			cv2.putText(img,'Sharp Image', (0, 50), font, 0.5, (255,255, 69), 2)

        # Display the image
	plt.imshow(img)
	plt.title(filename)
	plt.show()
	
#### Please keep clicking on the "x" or close window option to view the next processed image ####
