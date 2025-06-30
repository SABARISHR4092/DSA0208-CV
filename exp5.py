import cv2
import numpy as np

# Step 1: Read the image
image = cv2.imread('C:\Users\antoc\OneDrive\Desktop\Course CV\LAB\src\img1.png')  # Replace with your image file

# Step 2: Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Create a kernel for erosion
kernel = np.ones((5, 5), np.uint8)  # You can adjust the size for different effects

# Step 4: Apply erosion
eroded_image = cv2.erode(gray_image, kernel, iterations=1)

# Step 5: Display original and eroded images
cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', eroded_image)

# Step 6: Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
