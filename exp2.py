import cv2

# Read the image
image = cv2.imread(r"C:\Users\antoc\OneDrive\Desktop\Course CV\LAB\src\img1.png")  # Replace with your image filename

# Check if image is loaded
if image is None:
    print("Error: Image not found or unable to read.")
else:
    # Display the original image
    cv2.imshow('Original Image', image)

    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)  # (15,15) is kernel size

    # Display the blurred image
    cv2.imshow('Blurred Image', blurred_image)

    # Save the blurred image (optional)
    cv2.imwrite('blurred_output.jpg', blurred_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
