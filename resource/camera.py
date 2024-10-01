import cv2
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage


class CameraThread(QThread):
    image_update = pyqtSignal(QImage)

    def __init__(self):
        super().__init__()
        self._is_running = True

    def run(self):
        cap = cv2.VideoCapture(0)
        while self._is_running:
            ret, frame = cap.read()
            if ret:
                # Convert the image to RGB format
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Convert to QImage
                h, w, ch = frame.shape
                bytes_per_line = ch * w
                q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                self.image_update.emit(q_img)
        cap.release()

    def stop(self):
        """Stops the camera thread."""
        self._is_running = False
        self.wait()