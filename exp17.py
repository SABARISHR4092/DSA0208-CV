import cv2
import numpy as np

# Read the image
image = cv2.imread(r'C:\Users\antoc\OneDrive\Desktop\Course CV\LAB\src\img3.jpg')  # Replace with your image filename

# Check if image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Sobel filter along X-axis
sobel_x = cv2.Sobel(gray, cv2.CV_64F, dx=1, dy=0, ksize=3)

# Convert to absolute values and then to uint8
abs_sobel_x = cv2.convertScaleAbs(sobel_x)

# Display results
cv2.imshow('Original Image', image)
cv2.imshow('Sobel X Edge Detection', abs_sobel_x)

# Save output (optional)
cv2.imwrite('sobel_x_edges.jpg', abs_sobel_x)

cv2.waitKey(0)
cv2.destroyAllWindows()
