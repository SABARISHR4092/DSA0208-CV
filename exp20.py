import cv2
import numpy as np

# Read the original image
image = cv2.imread(r'C:\Users\antoc\OneDrive\Desktop\Course CV\LAB\src\img3.jpg')  # Replace with your image path

# Check if image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Convert to grayscale (sharpening often applied to single channel)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define Laplacian kernel with negative center coefficient (common sharpening kernel)
laplacian_kernel = np.array([[0,  -1,  0],
                             [-1,  5, -1],
                             [0,  -1,  0]])

# Apply filter2D with the sharpening kernel
sharpened = cv2.filter2D(gray, -1, laplacian_kernel)

# Display the original and sharpened images
cv2.imshow('Original Grayscale Image', gray)
cv2.imshow('Sharpened Image (Laplacian Mask)', sharpened)

# Save the result (optional)
cv2.imwrite('sharpened_laplacian.jpg', sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
