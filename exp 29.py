import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread("C:\\Users\\user\\OneDrive\\Documents\\Computer vision with openCV\\image3.jpg", 0)

# Define a kernel
kernel = np.ones((5,5), np.uint8)

# Apply erosion
eroded = cv2.erode(img, kernel, iterations=1)

# Show result
cv2.imshow('Eroded Image', eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()
