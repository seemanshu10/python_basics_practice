import sys 

from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QLineEdit, QTextEdit, QPushButton)

from PySide2.QtCore import Slot, Qt

@Slot()
def save_note():
    status_label.setText("Status: Note Saved Successfully.")

@Slot()
def names_inputs():
    name = student_name_line.text().strip()
    if name:
        save_button.setEnabled(True)
    else:
        save_button.setEnabled(False)
    
    if name:
        status_label.setText(f"Status: Typing name - {name}")
    else:
        status_label.setText("Status: Waiting for input")

@Slot()
def notes_inputs():

    note = notes_textbox.toPlainText()
    if note:
        save_button.setEnabled(True)
    else:
        save_button.setEnabled(False)
    
    if note:
        status_label.setText(f"Status: Note {note}")
    else:
        status_label.setText("Status: Waiting for input")
    
@Slot()
def clear_ui():
    student_name_line.setText("")
    notes_textbox.setText("")
    status_label.setText("Status: All Fields Cleared")
    save_button.setEnabled(False)


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Student Notes App")
window.resize(500, 500)

label = QLabel("Student Notes App")

# Student Layout 
student_layout = QHBoxLayout()
student_label = QLabel("Student Name:")
student_name_line = QLineEdit()
student_name_line.setPlaceholderText("Enter the Student name")

student_layout.addWidget(student_label)
student_layout.addWidget(student_name_line)

# notes layout 
notes_label = QLabel("Notes:")

notes_textbox = QTextEdit()
notes_textbox.setPlaceholderText("Enter the notes here")

button_layout = QHBoxLayout()
save_button = QPushButton("Save Note")
save_button.setEnabled(False)
clear_button = QPushButton("Clear")

button_layout.addWidget(save_button)
button_layout.addWidget(clear_button)

# Status layout 
status_label = QLabel("Status: Waiting For Input")

main_layout = QVBoxLayout()
main_layout.addWidget(label, alignment= Qt.AlignCenter)
main_layout.addLayout(student_layout)
main_layout.addWidget(notes_label)
main_layout.addWidget(notes_textbox)
main_layout.addLayout(button_layout)
main_layout.addWidget(status_label)

window.setLayout(main_layout)

# connection 
clear_button.clicked.connect(clear_ui)
save_button.clicked.connect(save_note)
student_name_line.textChanged.connect(names_inputs)
notes_textbox.textChanged.connect(notes_inputs)

# display window
window.show()
sys.exit(app.exec_())