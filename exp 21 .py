import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image (grayscale)
img = cv2.imread('your_image.jpg', cv2.IMREAD_GRAYSCALE)

# Define the extended Laplacian kernel
laplacian_kernel = np.array([[1, 1, 1],
                             [1, -8, 1],
                             [1, 1, 1]])

# Apply Laplacian
laplacian = cv2.filter2D(img, -1, laplacian_kernel)

# Sharpened image = Original - Laplacian (or + based on sign convention)
sharpened = cv2.add(img, laplacian)

# Display
plt.figure(figsize=(10,4))
plt.subplot(1,3,1), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(1,3,2), plt.imshow(laplacian, cmap='gray'), plt.title('Laplacian')
plt.subplot(1,3,3), plt.imshow(sharpened, cmap='gray'), plt.title('Sharpened')
plt.tight_layout()
plt.show()
