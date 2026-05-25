import cv2
import pyttsx3

# voice engine
engine = pyttsx3.init()

# mobile camera stream URL
# yahan apna IP Webcam wala URL dalna
url = "http://YOUR_IP:8080/video"

cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera not connected")
        break

    cv2.imshow("Blind Assist Camera", frame)

    # press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

engine.say("Camera started successfully")
engine.runAndWait()

cap.release()
cv2.destroyAllWindows()
