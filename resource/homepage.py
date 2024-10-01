from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from resource.camera import CameraThread


class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.camera_thread = CameraThread()
        self.camera_thread.image_update.connect(self.update_image)
        self.camera_thread.start()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

    def update_image(self, q_image):
        self.image_label.setPixmap(QPixmap.fromImage(q_image))

    def closeEvent(self, event):
        self.camera_thread.quit()
        self.camera_thread.wait()
        event.accept()