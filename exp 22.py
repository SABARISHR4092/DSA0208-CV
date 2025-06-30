from google.colab import files
uploaded = files.upload()
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Use the exact name from uploaded.keys()
img = cv2.imread("Screenshot 2025-06-29 185752.png", cv2.IMREAD_GRAYSCALE)

if img is None:
    raise ValueError("Image not loaded. Check file name.")

laplacian_kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

laplacian = cv2.filter2D(img, -1, laplacian_kernel)
sharpened = cv2.add(img, laplacian)

plt.figure(figsize=(12,4))
plt.subplot(1,3,1), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(1,3,2), plt.imshow(laplacian, cmap='gray'), plt.title('Laplacian')
plt.subplot(1,3,3), plt.imshow(sharpened, cmap='gray'), plt.title('Sharpened')
plt.tight_layout()
plt.show()
