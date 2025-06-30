import cv2

# Load the image
img = cv2.imread("C:\\Users\\user\\OneDrive\\Documents\\Computer vision with openCV\\image3.jpg")

# Add watermark text
cv2.putText(img, 'Watermark', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
            1, (255, 255, 255), 2, cv2.LINE_AA)

# Save or display the watermarked image
cv2.imwrite("C:\\Users\\user\\OneDrive\\Documents\\Computer vision with openCV\\watermark.png", img)
cv2.imshow('Watermarked', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
