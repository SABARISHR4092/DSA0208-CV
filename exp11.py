import cv2
import numpy as np

# Read the original image
image = cv2.imread(r'C:\Users\antoc\OneDrive\Desktop\Course CV\LAB\src\img3.jpg')  # Replace with your image path

# Check if the image is loaded
if image is None:
    print("Error: Image not found or unable to read.")
    exit()

# Get the dimensions
rows, cols = image.shape[:2]

# Define 3 points from the original image
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

# Define where those 3 points should move to (destination points)
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Get the Affine Transformation matrix
M = cv2.getAffineTransform(pts1, pts2)

# Apply the transformation
affine_transformed = cv2.warpAffine(image, M, (cols, rows))

# Display results
cv2.imshow('Original Image', image)
cv2.imshow('Affine Transformed Image', affine_transformed)

# Save transformed image (optional)
cv2.imwrite('affine_transformed.jpg', affine_transformed)

# Wait and close
cv2.waitKey(0)
cv2.destroyAllWindows()
