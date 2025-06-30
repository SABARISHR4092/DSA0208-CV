import cv2
import numpy as np

# Read the image
image = cv2.imread(r'C:\Users\antoc\OneDrive\Desktop\Course CV\LAB\src\img3.jpg')  # Replace with your image filename

# Check if the image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Sobel filter along Y-axis
sobel_y = cv2.Sobel(gray, cv2.CV_64F, dx=0, dy=1, ksize=3)

# Convert result to absolute values and then to 8-bit format
abs_sobel_y = cv2.convertScaleAbs(sobel_y)

# Display results
cv2.imshow('Original Image', image)
cv2.imshow('Sobel Y Edge Detection', abs_sobel_y)

# Save the output (optional)
cv2.imwrite('sobel_y_edges.jpg', abs_sobel_y)

cv2.waitKey(0)
cv2.destroyAllWindows()
