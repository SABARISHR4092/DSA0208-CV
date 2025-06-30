import cv2
import numpy as np

# Read the image
image = cv2.imread(r'C:\Users\antoc\OneDrive\Desktop\Course CV\LAB\src\img2.jpg')  # Replace with your image file

# Check if image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Sobel filter along X and Y axes
sobel_x = cv2.Sobel(gray, cv2.CV_64F, dx=1, dy=0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, dx=0, dy=1, ksize=3)

# Combine both directions: magnitude = sqrt(sobel_x^2 + sobel_y^2)
sobel_xy = cv2.magnitude(sobel_x, sobel_y)

# Convert to 8-bit format
sobel_xy = cv2.convertScaleAbs(sobel_xy)

# Display results
cv2.imshow('Original Image', image)
cv2.imshow('Sobel XY Edge Detection', sobel_xy)

# Save the result (optional)
cv2.imwrite('sobel_xy_edges.jpg', sobel_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()
