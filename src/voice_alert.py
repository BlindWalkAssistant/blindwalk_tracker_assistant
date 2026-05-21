# import pyttsx3
# import threading
# import queue

# engine = pyttsx3.init()

# speech_queue = queue.Queue()


# def voice_worker():
#     while True:
#         text = speech_queue.get()
#         if text is None:
#             break

#         engine.say(text)
#         engine.runAndWait()
#         speech_queue.task_done()


# thread = threading.Thread(target=voice_worker, daemon=True)
# thread.start()


# def speak(text):
#     speech_queue.put(text)

import cv2
import pyttsx3
import threading
import queue
import time
from ultralytics import YOLO

# ---------------- VOICE ----------------

engine = pyttsx3.init()

speech_queue = queue.Queue()

def voice_worker():

    while True:

        text = speech_queue.get()

        if text is None:
            break

        engine.say(text)
        engine.runAndWait()

threading.Thread(target=voice_worker, daemon=True).start()

def speak(text):

    # old voice remove
    while not speech_queue.empty():
        try:
            speech_queue.get_nowait()
        except:
            pass

    speech_queue.put(text)

# ---------------- MODEL ----------------

model = YOLO("yolov8n.pt")

# ---------------- CAMERA ----------------

cap = cv2.VideoCapture(0)

# ---------------- SETTINGS ----------------

KNOWN_WIDTH = 14      # cm (example object width)
FOCAL_LENGTH = 700    # adjust after calibration

last_spoken = ""
last_time = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    nearest_object = None
    nearest_distance = 999999

    for r in results:

        boxes = r.boxes

        for box in boxes:

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            w = x2 - x1

            cls = int(box.cls[0])

            label = model.names[cls]

            # ---------------- DISTANCE ----------------

            # distance = (real width × focal length) / pixel width
            distance = (KNOWN_WIDTH * FOCAL_LENGTH) / w

            # ---------------- DRAW ----------------

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0,255,0),
                2
            )

            cv2.putText(
                frame,
                f"{label} {distance:.1f} cm",
                (x1, y1-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0,255,0),
                2
            )

            # nearest object
            if distance < nearest_distance:

                nearest_distance = distance
                nearest_object = label

    # ---------------- VOICE ALERT ----------------

    current_time = time.time()

    # Speak only if object comes close
    if nearest_object and nearest_distance < 80:

        text = f"{nearest_object} is {int(nearest_distance)} centimeters away"

        if (
            text != last_spoken
            or current_time - last_time > 3
        ):

            speak(text)

            last_spoken = text
            last_time = current_time

    cv2.imshow("Live Object Distance Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ---------------- CLEANUP ----------------

speech_queue.put(None)

cap.release()
cv2.destroyAllWindows()