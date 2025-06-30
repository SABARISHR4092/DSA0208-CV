import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread("C:\\Users\\user\\OneDrive\\Documents\\Computer vision with openCV\\image5.jpg", 0)

# Define kernel
kernel = np.ones((5,5), np.uint8)

# Apply dilation
dilated = cv2.dilate(img, kernel, iterations=1)

# Show result
cv2.imshow('Dilated Image', dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()
