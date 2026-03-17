import cv2
from ultralytics import YOLO

# load trained model
model = YOLO("models/best.pt")

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    results = model(frame, conf=0.45)

    annotated = results[0].plot()

    cv2.imshow("Blind Walk Assistant", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()