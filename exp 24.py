from google.colab import files
uploaded = files.upload()

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
img = cv2.imread("Screenshot 2025-06-30 094151.png", cv2.IMREAD_GRAYSCALE)

if img is None:
    raise ValueError("Image not loaded. Check the file path or name.")

# Define High-Boost Mask (A=2) → center = A + 8 = 10
high_boost_kernel = np.array([
    [-1, -1, -1],
    [-1, 10, -1],
    [-1, -1, -1]
])

# Apply High-Boost filter
sharpened = cv2.filter2D(img, -1, high_boost_kernel)

# Show the results
plt.figure(figsize=(10,4))
plt.subplot(1,2,1), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(1,2,2), plt.imshow(sharpened, cmap='gray'), plt.title('High-Boost Sharpened (A=2)')
plt.tight_layout()
plt.show()
