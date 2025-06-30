import cv2

# Read the image
image = cv2.imread(r'C:\Users\antoc\OneDrive\Desktop\Course CV\LAB\src\img3.jpg')  # Replace with your image filename

# Check if image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Convert to grayscale (Canny works on single channel)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 1.4)

# Apply Canny edge detection
# Threshold1 and Threshold2 can be tuned
edges = cv2.Canny(blurred, threshold1=50, threshold2=150)

# Display results
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edge Detection', edges)

# Save result (optional)
cv2.imwrite('canny_edges.jpg', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
