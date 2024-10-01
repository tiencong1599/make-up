from PyQt5.QtCore import QObject, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from resource.camera import CameraThread


class CameraControl(QWidget):
    def __init__(self):
        super().__init__()

        self.camera_thread = None

        # Layout and UI setup
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Camera feed label
        self.camera_label = QLabel("Camera feed will appear here")
        layout.addWidget(self.camera_label)

        # Start Camera button
        self.start_button = QPushButton("Start Camera", self)
        self.start_button.clicked.connect(self.start_camera_thread)
        layout.addWidget(self.start_button)

        # Stop Camera button
        self.stop_button = QPushButton("Stop Camera", self)
        self.stop_button.clicked.connect(self.stop_camera_thread)
        layout.addWidget(self.stop_button)

        self.setLayout(layout)

    def start_camera_thread(self):
        """Start the camera thread."""
        if self.camera_thread is None:
            self.camera_thread = CameraThread()
            self.camera_thread.image_update.connect(self.update_image)
            self.camera_thread.start()

    def stop_camera_thread(self):
        """Stop the camera thread."""
        if self.camera_thread is not None:
            self.camera_thread.stop()
            self.camera_thread = None
            self.init_ui()

    def update_image(self, q_img):
        """Update the QLabel with the camera feed."""
        self.camera_label.setPixmap(QPixmap.fromImage(q_img))
        self.camera_label.setAlignment(Qt.AlignCenter)