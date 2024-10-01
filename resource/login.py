from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton
from handlers.handlers import MyHandler


class LoginPage(QWidget):
    def __init__(self, switch_to_main):
        super().__init__()
        self.switch_to_main = switch_to_main
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.handle_login)
        layout.addWidget(self.login_button)

        self.message_label = QLabel("", self)
        layout.addWidget(self.message_label)

        self.setLayout(layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        handler = MyHandler()
        is_successful = handler.login({
            'username': username,
            'password': password
        })

        if is_successful is True:
            self.message_label.setText("Login Successful!")
            # Switch to main page
            self.switch_to_main()

        else: self.message_label.setText("Invalid credentials")