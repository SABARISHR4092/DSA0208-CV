import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image in grayscale
img = cv2.imread("C:\\Users\\user\\OneDrive\\Documents\\Computer vision with openCV\\image2.jpg", cv2.IMREAD_GRAYSCALE)

# Define a simple edge-detection kernel (Laplacian)
kernel = np.array([[0, -1,  0],
                   [-1,  4, -1],
                   [0, -1,  0]])

# Apply convolution
edges = cv2.filter2D(img, -1, kernel)

# Show result
plt.imshow(edges, cmap='gray')
plt.title('Image Boundary'), plt.axis('off')
plt.show()
