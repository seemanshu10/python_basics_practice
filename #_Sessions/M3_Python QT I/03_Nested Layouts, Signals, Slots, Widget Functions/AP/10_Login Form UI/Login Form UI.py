# Login Form UI with Validation

import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton
from PySide2.QtCore import Slot, Qt

@Slot()
def validate_inputs():
    user = username.text().strip()
    password = password_text.text().strip()
    if user and password:
        login_btn.setEnabled(True)
    else:
        login_btn.setEnabled(False)


app = QApplication()

window = QWidget()
window.setWindowTitle("Login Form")

main_layout = QVBoxLayout()

user_label = QLabel("Username:")
username = QLineEdit()

password_label = QLabel("Password:")
password_text = QLineEdit()
password_text.setEchoMode(QLineEdit.Password)

login_btn = QPushButton("Login")
login_btn.setEnabled(False)

main_layout.addWidget(user_label)
main_layout.addWidget(username)
main_layout.addWidget(password_label)
main_layout.addWidget(password_text)
main_layout.addWidget(login_btn)

# connection to UI 
username.textChanged.connect(validate_inputs)
password_text.textChanged.connect(validate_inputs)

window.setLayout(main_layout)

window.setFixedSize(250, 150)
window.show()

sys.exit(app.exec_())