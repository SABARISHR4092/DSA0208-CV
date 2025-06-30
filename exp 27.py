import cv2

# Load image
img = cv2.imread("C:\\Users\\user\\OneDrive\\Documents\\Computer vision with openCV\\image5.jpg")

# Crop a region (y1:y2, x1:x2)
crop = img[50:150, 100:200]

# Get height and width of the cropped region
h, w, _ = crop.shape

# Make sure the destination fits inside the original image
if img.shape[0] > 200 + h and img.shape[1] > 300 + w:
    # Paste the cropped region at new location
    img[200:200+h, 300:300+w] = crop
else:
    print("Destination region is out of bounds!")

# Show and save result
cv2.imshow('Pasted Image', img)
cv2.imwrite('pasted_output.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
