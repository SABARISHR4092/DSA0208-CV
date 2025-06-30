import cv2

# Read the original image
image = cv2.imread(r'C:\Users\antoc\OneDrive\Desktop\Course CV\LAB\src\img3.jpg')  # Replace with your image file

# Check if image is loaded
if image is None:
    print("Error: Image not found or unable to read.")
    exit()

# Get image height and width
(h, w) = image.shape[:2]
center = (w // 2, h // 2)

# Rotate 90 degrees clockwise
clockwise_matrix = cv2.getRotationMatrix2D(center, -90, 1.0)
clockwise_rotated = cv2.warpAffine(image, clockwise_matrix, (w, h))

# Rotate 90 degrees counter-clockwise
counter_matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
counter_rotated = cv2.warpAffine(image, counter_matrix, (w, h))

# Display images
cv2.imshow('Original Image', image)
cv2.imshow('Clockwise Rotation (90°)', clockwise_rotated)
cv2.imshow('Counter-Clockwise Rotation (90°)', counter_rotated)

# Save rotated images (optional)
cv2.imwrite('rotated_clockwise.jpg', clockwise_rotated)
cv2.imwrite('rotated_counter.jpg', counter_rotated)

# Wait for key press and close
cv2.waitKey(0)
cv2.destroyAllWindows()
