

import cv2
import time
from ultralytics import YOLO
from src.voice_alert import speak
from src.distance_estimator import estimate_distance

# Load model
model = YOLO("models/best.pt")
names = model.names

cap = cv2.VideoCapture(0)

last_spoken_time = 0
last_message = ""

while True:

    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape

    # YOLO tracking
    results = model.track(
        frame,
        conf=0.25,
        imgsz=640,
        persist=True,
        tracker="bytetrack.yaml"
    )

    boxes = results[0].boxes

    closest_box = None
    largest_area = 0

    if boxes is not None:

        # find closest object
        for box in boxes:

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            area = (x2 - x1) * (y2 - y1)

            if area > largest_area:
                largest_area = area
                closest_box = box

        if closest_box is not None:

            x1, y1, x2, y2 = map(int, closest_box.xyxy[0])

            cls = int(closest_box.cls[0])
            label = names[cls]

            # direction detection
            center_x = (x1 + x2) // 2

            if center_x < w/3:
                direction = "LEFT"
            elif center_x > 2*w/3:
                direction = "RIGHT"
            else:
                direction = "FRONT"

            # distance estimation
            box_height = y2 - y1
            distance = estimate_distance(box_height)

            text = f"{label} {direction} {distance}"

            # voice cooldown
            if text != last_message and time.time() - last_spoken_time > 2:
                speak(text)
                last_spoken_time = time.time()
                last_message = text

            cv2.putText(
                frame,
                text,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

    annotated = results[0].plot()

    cv2.imshow("Blind Walk Assistant", annotated)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()