from google.colab import files
uploaded = files.upload()

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image (grayscale)
img = cv2.imread("Screenshot 2025-06-30 091514.png", cv2.IMREAD_GRAYSCALE)

if img is None:
    raise ValueError("Image not loaded. Check file name or path.")

# Step 1: Blur the image
blurred = cv2.GaussianBlur(img, (9, 9), 0)

# Step 2: Create unsharp mask
unsharp_mask = cv2.subtract(img, blurred)

# Step 3: Add unsharp mask to original image
alpha = 1.5  # control sharpening strength
sharpened = cv2.addWeighted(img, 1.0, unsharp_mask, alpha, 0)

# Display results
plt.figure(figsize=(12,4))
plt.subplot(1,3,1), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(1,3,2), plt.imshow(unsharp_mask, cmap='gray'), plt.title('Unsharp Mask')
plt.subplot(1,3,3), plt.imshow(sharpened, cmap='gray'), plt.title('Sharpened')
plt.tight_layout()
plt.show()
