import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in grayscale
img = cv2.imread("C:\\Users\\user\\OneDrive\\Documents\\Computer vision with openCV\\image2.jpg", cv2.IMREAD_GRAYSCALE)

# Define gradient masks (Prewitt-like)
gx = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]])

gy = np.array([[-1, -2, -1],
               [ 0,  0,  0],
               [ 1,  2,  1]])

# Apply convolution
grad_x = cv2.filter2D(img, -1, gx)
grad_y = cv2.filter2D(img, -1, gy)

# Combine gradients (magnitude)
sharpened = cv2.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)

# Display results
plt.subplot(1,2,1), plt.title("Original"), plt.imshow(img, cmap='gray'), plt.axis('off')
plt.subplot(1,2,2), plt.title("Gradient Sharpened"), plt.imshow(sharpened, cmap='gray'), plt.axis('off')
plt.tight_layout(), plt.show()
