import cv2

# Open the webcam (0 = default camera)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Ask user for playback mode
print("Select Webcam Playback Mode:")
print("1. Normal Speed")
print("2. Slow Motion")
print("3. Fast Motion")
mode = input("Enter option (1/2/3): ")

# Set delay time based on mode
if mode == '1':
    delay = int(1000 / 30)  # Normal: ~30 FPS
elif mode == '2':
    delay = int(1000 / 10)  # Slow Motion: ~10 FPS
elif mode == '3':
    delay = int(1000 / 60)  # Fast Motion: ~60 FPS
else:
    print("Invalid option. Defaulting to Normal Speed.")
    delay = int(1000 / 30)

print("Press 'q' to quit.")

# Read frames continuously
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Show the frame
    cv2.imshow('Webcam Video', frame)

    # Wait for delay time, break if 'q' is pressed
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

# Release webcam and close windows
cap.release()
cv2.destroyAllWindows()
