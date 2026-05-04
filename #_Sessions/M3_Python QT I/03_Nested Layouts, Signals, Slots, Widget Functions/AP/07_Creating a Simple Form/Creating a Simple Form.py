# Creating a Simple Form
import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PySide2.QtCore import Slot

@Slot()
def typing_text():
    status_label.setText("Enter Your name:")

@Slot()
def submit_fields():
    text_field = name_text.text()

    status_label.setText(f"Hello, {text_field}!")

app = QApplication()

window = QWidget()
window.setWindowTitle("Simple Form")

window.setFixedSize(400,250)

main_layout = QVBoxLayout()

status_label = QLabel()
# label_status.text()

name_text = QLineEdit()
name_text.setPlaceholderText("Enter Your Name.")

submit_btn = QPushButton("Submit")

main_layout.addWidget(status_label)
main_layout.addWidget(name_text)
main_layout.addWidget(submit_btn)

# connection 
name_text.textEdited.connect(typing_text)
submit_btn.clicked.connect(submit_fields)

window.setLayout(main_layout)
window.show()
sys.exit(app.exec_())