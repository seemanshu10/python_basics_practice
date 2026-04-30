import sys 

from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                               QLabel, QLineEdit, QTextEdit, QPushButton)


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Student Notes App")
window.resize(500, 500)

label = QLabel("Student Notes App")

student_name_line = QLineEdit()
student_name_line.setPlaceholderText("Enter the Student name")

notes_textbox = QTextEdit()
notes_textbox.setPlaceholderText("Enter the notes here")

save_button = QPushButton("Save Note")
clear_button = QPushButton("Clear")
# notes_textbox.

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(student_name_line)
layout.addWidget(notes_textbox)
layout.addWidget(save_button)
layout.addWidget(clear_button)

window.setLayout(layout)

# display window
window.show()
sys.exit(app.exec_())