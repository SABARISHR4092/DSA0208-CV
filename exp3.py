import cv2

# Step 1: Read the image
image = cv2.imread(r'C:\Users\antoc\OneDrive\Desktop\Course CV\LAB\src\img1.png')  # Replace with your actual image filename

# Step 2: Convert to grayscale (Canny works on single channel)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply Gaussian Blur to reduce noise (optional but improves result)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Step 4: Apply Canny edge detection
edges = cv2.Canny(blurred_image, threshold1=50, threshold2=150)

# Step 5: Display original and edge-detected images
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edge Detection', edges)

# Step 6: Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
