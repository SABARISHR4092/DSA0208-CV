import cv2

# Read the original image
image = cv2.imread(r'C:\Users\antoc\OneDrive\Desktop\Course CV\LAB\src\img1.png')  # Replace with your image path

# Check if image is loaded successfully
if image is None:
    print("Error: Image not found or unable to read.")
    exit()

# Scale down (reduce size by 50%)
smaller_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Scale up (increase size by 150%)
bigger_image = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

# Display all images
cv2.imshow('Original Image', image)
cv2.imshow('Smaller Image (50%)', smaller_image)
cv2.imshow('Bigger Image (150%)', bigger_image)

# Save results (optional)
cv2.imwrite('scaled_smaller.jpg', smaller_image)
cv2.imwrite('scaled_bigger.jpg', bigger_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
