import sys 

from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QLineEdit, QTextEdit, QPushButton)

from PySide2.QtCore import Slot

@Slot()
def clear_ui():
    student_name_line.setText("")
    notes_textbox.setText("")

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Student Notes App")
window.resize(500, 500)

label = QLabel("Student Notes App")

student_name_line = QLineEdit()
student_name_line.setPlaceholderText("Enter the Student name")

notes_textbox = QTextEdit()
notes_textbox.setPlaceholderText("Enter the notes here")

button_layout = QHBoxLayout()
save_button = QPushButton("Save Note")
clear_button = QPushButton("Clear")

button_layout.addWidget(save_button)
button_layout.addWidget(clear_button)
# notes_textbox.

main_layout = QVBoxLayout()
main_layout.addWidget(label)
main_layout.addWidget(student_name_line)
main_layout.addWidget(notes_textbox)
main_layout.addLayout(button_layout)

window.setLayout(main_layout)

# connection 
clear_button.clicked.connect(clear_ui)

# display window
window.show()
sys.exit(app.exec_())