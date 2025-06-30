import cv2
import numpy as np

# Read the image
image = cv2.imread(r'C:\Users\antoc\OneDrive\Desktop\Course CV\LAB\src\img3.jpg')  # Replace with your image path

# Check if image is loaded
if image is None:
    print("Error: Image not found or unable to read.")
    exit()

# Define the translation values
# Move image 100 pixels right and 50 pixels down
tx = 100  # shift along X-axis
ty = 50   # shift along Y-axis

# Create the translation matrix
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

# Get the image dimensions
height, width = image.shape[:2]

# Apply the translation
translated_image = cv2.warpAffine(image, translation_matrix, (width + tx, height + ty))

# Show original and translated image
cv2.imshow('Original Image', image)
cv2.imshow('Moved Image', translated_image)

# Save translated image (optional)
cv2.imwrite('translated_image.jpg', translated_image)

# Wait and close
cv2.waitKey(0)
cv2.destroyAllWindows()
