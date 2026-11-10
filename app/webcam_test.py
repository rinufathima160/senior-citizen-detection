
import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not access webcam.")
    exit()

# Set camera resolution
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Create a full-screen window
cv2.namedWindow("Webcam Test", cv2.WINDOW_NORMAL)
cv2.setWindowProperty(
    "Webcam Test",
    cv2.WND_PROP_FULLSCREEN,
    cv2.WINDOW_FULLSCREEN
)

print("Webcam started. Press Q to quit.")

while True:
    ret, frame = camera.read()

    if not ret:
        print("Failed to capture frame.")
        break

    # Resize frame to fit the screen
    frame = cv2.resize(frame, (1280, 720))

    cv2.imshow("Webcam Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
