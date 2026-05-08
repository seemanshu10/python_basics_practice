# Building a GUI for File Management

import sys

from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                               QPushButton, QLabel, QLineEdit)

def open_file_func():
    file_path = file_path_input_textbox.text()

    status_message_label.setText(f"File Opened: {file_path}")

def delete_file_func():
    file_path = file_path_input_textbox.text()

    status_message_label.setText(f"File deleted: {file_path}")

# create application object 
app = QApplication(sys.argv)

# set window settings 
window = QWidget()
window.setWindowTitle("File Management Tool")
window.resize(400,300)

file_path_input_textbox = QLineEdit()
file_path_input_textbox.setPlaceholderText("Enter File Path..")

status_message_label = QLabel("File Info Will Appear Here.")

open_button = QPushButton("Open File")
delete_button = QPushButton("Delete File")

# layout Setup
layout = QVBoxLayout()
layout.addWidget(file_path_input_textbox)
layout.addWidget(status_message_label)
layout.addWidget(open_button)
layout.addWidget(delete_button)

window.setLayout(layout)

# call The Function when buttom pressed 
open_button.clicked.connect(open_file_func)
delete_button.clicked.connect(delete_file_func)

window.show()
sys.exit(app.exec_())
