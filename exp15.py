import cv2
import numpy as np

def compute_homography_dlt(src_pts, dst_pts):
    """
    Computes the homography matrix using Direct Linear Transformation (DLT).
    src_pts and dst_pts should be 4x2 arrays.
    """
    A = []
    for (x, y), (x_prime, y_prime) in zip(src_pts, dst_pts):
        A.append([-x, -y, -1, 0, 0, 0, x * x_prime, y * x_prime, x_prime])
        A.append([0, 0, 0, -x, -y, -1, x * y_prime, y * y_prime, y_prime])
    
    A = np.asarray(A)
    # Solve Ah = 0 using SVD
    U, S, Vt = np.linalg.svd(A)
    H = Vt[-1].reshape(3, 3)
    return H / H[2, 2]

# Load the image
image = cv2.imread(r'C:\Users\antoc\OneDrive\Desktop\Course CV\LAB\src\img3.jpg')  # Replace with your image
if image is None:
    print("Error: Could not load image.")
    exit()

h, w = image.shape[:2]

# Define 4 source and destination points
src_pts = np.float32([[100, 100], [w - 100, 100], [100, h - 100], [w - 150, h - 150]])
dst_pts = np.float32([[0, 0], [w, 0], [0, h], [w, h]])

# Compute homography using DLT
H_dlt = compute_homography_dlt(src_pts, dst_pts)

# Apply transformation
transformed_img = cv2.warpPerspective(image, H_dlt, (w, h))

# Display results
cv2.imshow("Original Image", image)
cv2.imshow("DLT Homography Transformed", transformed_img)
cv2.imwrite("dlt_transformed.jpg", transformed_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
