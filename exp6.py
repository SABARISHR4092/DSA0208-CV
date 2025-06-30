import cv2

# Load the captured video
video_path = r'C:\Users\antoc\OneDrive\Desktop\Course CV\LAB\src\reflex.mp4'  # Replace with your video file
cap = cv2.VideoCapture(video_path)

# Check if the video was opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Ask user for playback mode
print("Select Playback Mode:")
print("1. Normal Speed")
print("2. Slow Motion")
print("3. Fast Motion")
mode = input("Enter option (1/2/3): ")

# Set delay time based on mode
if mode == '1':
    delay = int(1000 / 30)  # Normal: 30 FPS
elif mode == '2':
    delay = int(1000 / 10)  # Slow Motion: ~10 FPS
elif mode == '3':
    delay = int(1000 / 60)  # Fast Motion: ~60 FPS
else:
    print("Invalid option. Playing at normal speed.")
    delay = int(1000 / 30)

# Read and display frames
while True:
    ret, frame = cap.read()
    if not ret:
        break  # Video has ended

    cv2.imshow('Video Playback', frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

# Release video and close windows
cap.release()
cv2.destroyAllWindows()
