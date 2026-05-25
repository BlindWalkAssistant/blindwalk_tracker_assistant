import cv2
import pyttsx3

# ---------------------------------------------------
# Mobile Camera URL
# Replace with your IP Webcam address
# Example: http://192.168.1.5:8080/video
# ---------------------------------------------------
CAMERA_URL = "http://YOUR_IP:8080/video"


# Voice Engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)


def speak(text):
    engine.say(text)
    engine.runAndWait()


# Open mobile camera stream
cap = cv2.VideoCapture(CAMERA_URL)

if not cap.isOpened():
    print("Error: Could not connect to mobile camera.")
    exit()

print("Mobile Camera Connected Successfully")
speak("Camera connected successfully")

last_message = ""

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    # Display camera frame
    cv2.imshow("Blind Assist - Mobile Camera", frame)

    # Dummy detected object text
    detected_object = "Object detected"

    # Show text on screen
    cv2.putText(
        frame,
        detected_object,
        (40, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Speak only once
    if detected_object != last_message:
        speak(detected_object)
        last_message = detected_object

    # Press ESC to exit
    if cv2.waitKey(1) == 27:
        break


cap.release()
cv2.destroyAllWindows()