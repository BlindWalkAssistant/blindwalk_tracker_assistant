from ultralytics import YOLO

class Tracker:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def track(self, frame):
        results = self.model.track(frame, persist=True)
        return results