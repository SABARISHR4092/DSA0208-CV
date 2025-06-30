import cv2

# Read the original image
image = cv2.imread(r"C:\Users\antoc\OneDrive\Desktop\Course CV\LAB\src\img1.png")  # Replace with your image file name

# Check if image is loaded
if image is None:
    print("Error: Image not found or unable to read.")
else:
    # Display the original image
    cv2.imshow('Original Image', image)

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the grayscale image
    cv2.imshow('Grayscale Image', gray_image)

    # Save the grayscale image (optional)
    cv2.imwrite('grayscale_output.jpg', gray_image)

    # Wait until a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()
