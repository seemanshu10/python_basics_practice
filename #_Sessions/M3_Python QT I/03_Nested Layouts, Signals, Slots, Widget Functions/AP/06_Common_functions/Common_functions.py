# Common_Functions

import sys

from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                               QPushButton, QLabel, QRadioButton, QLineEdit, QCheckBox)

from PySide2.QtCore import Qt, Slot

@Slot()
def typing_text():
    status_label.setText("Submitted: Text Will Appear Here.")

@Slot()
def toggle_field():
    input_line.setEnabled(enableinput_chkbox.isChecked())

@Slot()
def toggle_show_input():
    input_line.setVisible(showinput_chkbox.isChecked())

@Slot()
def clear_text():
    input_line.clear()

@Slot()
def reset_fields():
    input_line.setText("")
    enableinput_chkbox.setChecked(True)
    showinput_chkbox.setChecked(True)
    lowercase_radbox.setChecked(True)

    status_label.setText(f"Submitted: Reset Fields.")

@Slot()
def submit_fields():
    text_field = input_line.text()

    if lowercase_radbox.isChecked():
        text_field = text_field.lower()

    elif uppercase_radbox.isChecked():
        text_field = text_field.upper()

    status_label.setText(f"Submitted: {text_field}")

# define app
app = QApplication()

window = QWidget()
window.setWindowTitle("Common Widget Functions")

main_layout = QVBoxLayout()

# input layout 
input_layout = QHBoxLayout()

input_label = QLabel("Input Field:")
input_line = QLineEdit()
input_line.setPlaceholderText("Type Something Here..")

input_layout.addWidget(input_label)
input_layout.addWidget(input_line)

# checkbox layout
show_layout = QHBoxLayout()

enableinput_chkbox = QCheckBox("Enable Input")
showinput_chkbox = QCheckBox("Show Input")

enableinput_chkbox.setChecked(True)
showinput_chkbox.setChecked(True)

show_layout.addWidget(enableinput_chkbox)
show_layout.addWidget(showinput_chkbox)

# radio layout
case_layout = QHBoxLayout()

uppercase_radbox = QRadioButton("Uppercase")
lowercase_radbox = QRadioButton("Lowercase")

case_layout.addWidget(uppercase_radbox)
case_layout.addWidget(lowercase_radbox)

# button layout added 
button_layout = QHBoxLayout()

clear_btn = QPushButton("Clear")
reset_btn = QPushButton("Reset")
submit_btn = QPushButton("Submit")

button_layout.addWidget(clear_btn)
button_layout.addWidget(reset_btn)
button_layout.addWidget(submit_btn)

# label - sumitted results
status_label = QLabel("Submitted: ")

# main Layout creation
main_layout.addLayout(input_layout)
main_layout.addLayout(show_layout)
main_layout.addLayout(case_layout)
main_layout.addLayout(button_layout)
main_layout.addWidget(status_label)

# signal slot connections 

input_line.textEdited.connect(typing_text)
enableinput_chkbox.stateChanged.connect(toggle_field)
showinput_chkbox.stateChanged.connect(toggle_show_input)
clear_btn.clicked.connect(clear_text)
reset_btn.clicked.connect(reset_fields)
submit_btn.clicked.connect(submit_fields)

window.setLayout(main_layout)
window.show()
sys.exit(app.exec_())