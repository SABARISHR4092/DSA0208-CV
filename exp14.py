import cv2
import numpy as np

# Read the input image
image = cv2.imread(r'C:\Users\antoc\OneDrive\Desktop\Course CV\LAB\src\img3.jpg')  # Replace with your image file

# Check if the image loaded successfully
if image is None:
    print("Error: Image not found.")
    exit()

# Get image size
h, w = image.shape[:2]

# Define 4 points in the source image (e.g., corners of a tilted rectangle)
src_points = np.float32([[100, 100], [w - 100, 100], [100, h - 100], [w - 150, h - 150]])

# Define destination points (where the corners should map to – a rectangle)
dst_points = np.float32([[0, 0], [w, 0], [0, h], [w, h]])

# Compute the Homography matrix
H, status = cv2.findHomography(src_points, dst_points)

# Warp the image using the Homography matrix
homography_result = cv2.warpPerspective(image, H, (w, h))

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Homography Transformed Image', homography_result)

# Save the result (optional)
cv2.imwrite('homography_result.jpg', homography_result)

# Wait and close
cv2.waitKey(0)
cv2.destroyAllWindows()
