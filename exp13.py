import cv2
import numpy as np

# Open video (0 for webcam, or use a file path like 'video.mp4')
cap = cv2.VideoCapture(0)  # Replace with 'your_video.mp4' if using a video file

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Read one frame to get dimensions and define transformation points
ret, frame = cap.read()
if not ret:
    print("Error: Couldn't read frame.")
    exit()

height, width = frame.shape[:2]

# Define source points (corners of a quadrilateral in original frame)
pts1 = np.float32([[50, 50], [width - 50, 50], [50, height - 50], [width - 50, height - 50]])

# Define destination points (rectangle output)
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# Get the Perspective Transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

print("Press 'q' to quit...")

# Process video frame by frame
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply perspective transformation
    transformed_frame = cv2.warpPerspective(frame, matrix, (width, height))

    # Show both original and transformed frames
    cv2.imshow('Original Video', frame)
    cv2.imshow('Perspective Transformed Video', transformed_frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release and close
cap.release()
cv2.destroyAllWindows()
