# Common_Functions

import sys

from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                               QPushButton, QLabel, QRadioButton, QLineEdit, QCheckBox, QComboBox)

from PySide2.QtCore import Qt, Slot

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

show_layout.addWidget(enableinput_chkbox)
show_layout.addWidget(showinput_chkbox)

# radio layout
case_layout = QHBoxLayout()

uppercase_chkbox = QRadioButton("Uppercase")
lowercase_chkbox = QRadioButton("Lowercase")

case_layout.addWidget(uppercase_chkbox)
case_layout.addWidget(lowercase_chkbox)

# button layout added 
button_layout = QHBoxLayout()

clear_btn = QPushButton("Clear")
reset_btn = QPushButton("Reset")
submit_btn = QPushButton("Submit")

button_layout.addWidget(clear_btn)
button_layout.addWidget(reset_btn)
button_layout.addWidget(submit_btn)

# label - sumitted results
status_label = QLabel("Submitted ")

# main Layout creation
main_layout.addLayout(input_layout)
main_layout.addLayout(show_layout)
main_layout.addLayout(case_layout)
main_layout.addLayout(button_layout)
main_layout.addWidget(status_label)

# signal slot connections 


window.setLayout(main_layout)
window.show()
sys.exit(app.exec_())