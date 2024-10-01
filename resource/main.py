from PyQt5.QtWidgets import QMainWindow

from resource.homepage import MainPage
from resource.login import LoginPage
# from resource.newuser import RegisterNewUser


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Camera App")

        self.login_page = LoginPage(self.switch_to_main)
        self.setCentralWidget(self.login_page)

    def switch_to_main(self):
        self.main_page = MainPage()
        self.setCentralWidget(self.main_page)
