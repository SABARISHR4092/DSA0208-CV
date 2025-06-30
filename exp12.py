import cv2
import numpy as np

# Read the original image
image = cv2.imread(r'C:\Users\antoc\OneDrive\Desktop\Course CV\LAB\src\img3.jpg')  # Replace with your image path

# Check if image is loaded
if image is None:
    print("Error: Image not found or unable to read.")
    exit()

# Get dimensions of the image
rows, cols = image.shape[:2]

# Define four points from the original image (source points)
pts1 = np.float32([[50, 50], [cols - 50, 50], [50, rows - 50], [cols - 50, rows - 50]])

# Define the desired position of those four points (destination points)
pts2 = np.float32([[0, 0], [cols, 0], [0, rows], [cols, rows]])

# Get the Perspective Transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply the perspective transformation
perspective_transformed = cv2.warpPerspective(image, matrix, (cols, rows))

# Display the original and transformed images
cv2.imshow('Original Image', image)
cv2.imshow('Perspective Transformed Image', perspective_transformed)

# Save the result (optional)
cv2.imwrite('perspective_transformed.jpg', perspective_transformed)

# Wait and close
cv2.waitKey(0)
cv2.destroyAllWindows()
