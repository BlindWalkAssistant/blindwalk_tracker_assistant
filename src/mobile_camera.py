import cv2


class MobileCamera:

    def __init__(self, ip_address, width=640, height=480):

       
        self.url = f"http://{ip_address}:8080/video"

        self.cap = cv2.VideoCapture(self.url)

        self.width = width
        self.height = height

        if not self.cap.isOpened():
            raise Exception(
                f"Cannot connect to mobile camera at {self.url}"
            )

        print(f" Connected to Mobile Camera: {self.url}")

    def get_frame(self):

        ret, frame = self.cap.read()

        if not ret:
            return None

        frame = cv2.resize(frame, (self.width, self.height))

        return frame

    def release(self):

        self.cap.release()
        cv2.destroyAllWindows()