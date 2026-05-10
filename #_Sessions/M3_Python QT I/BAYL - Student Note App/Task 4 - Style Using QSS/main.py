import sys 

from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton)

from PySide2.QtCore import Qt, Slot

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):    
        # Window creating
        self.setWindowTitle("Student Notes App")

        self.label = QLabel("Student Notes App")

        self.label.setStyleSheet("""
            QLabel {
                font-size: 22px;
                font-weight: bold;
                padding: 10px;
            }
        """)

        # Student Layout 
        self.student_layout = QHBoxLayout()
        self.student_label = QLabel("Student Name:")
        self.student_label.setStyleSheet("""
            QLabel {
                font-size: 15px;
                padding: 2px;
            }
        """)

        self.student_name_line = QLineEdit()
        self.student_name_line.setPlaceholderText("Enter the Student name")

        self.student_name_line.setStyleSheet("""
            QLineEdit {
                color: black;
                border: 1px solid #485460;
                padding: 6px;
                border-radius: 8px;
            }
            QLineEdit:focus {
                border: 1px solid #00a8ff;
            }
        """)


        self.student_layout.addWidget(self.student_label)
        self.student_layout.addWidget(self.student_name_line)

        # notes layout 
        self.notes_label = QLabel("Notes:")

        self.notes_label.setStyleSheet("""
            QLabel {
                font-size: 15px;
                padding: 2px;
            }
        """)

        self.notes_textbox = QTextEdit()
        self.notes_textbox.setPlaceholderText("Write notes here....")

        self.notes_textbox.setStyleSheet("""
            QTextEdit {
                color: black;
                font-size: 15px;
                border: 1px solid #485460;
                padding: 6px;
                border-radius: 10px;
            }
            QTextEdit:focus {
                border: 1px solid purple;
            }
        """)


        self.button_layout = QHBoxLayout()
        self.save_button = QPushButton("Save Note")
        self.save_button.setEnabled(False)
        self.clear_button = QPushButton("Clear")

        self.save_button.setStyleSheet("""
            QPushButton {
                background-color: green;
                color: white;
                border-radius: 10px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1c5980;
            }
        """)

        self.clear_button.setStyleSheet("""
            QPushButton {
                background-color: red;
                color: white;
                border-radius: 10px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1c5980;
            }
        """)

        self.button_layout.addWidget(self.save_button)
        self.button_layout.addWidget(self.clear_button)

        # Status layout 
        self.status_label = QLabel("Status: Waiting For Input")
        self.setStyleSheet("""
            QLabel {
                font-family: Arial;
                font-style: italic;
            }
        """)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.label, alignment= Qt.AlignCenter)
        self.main_layout.addLayout(self.student_layout)
        self.main_layout.addWidget(self.notes_label)
        self.main_layout.addWidget(self.notes_textbox)
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addWidget(self.status_label)

        self.setLayout(self.main_layout)

        # connection 
        self.clear_button.clicked.connect(self.clear_ui)
        self.save_button.clicked.connect(self.save_note)
        self.student_name_line.textChanged.connect(self.names_inputs)
        self.notes_textbox.textChanged.connect(self.notes_inputs)

    @Slot()
    def save_note(self):
        self.status_label.setText("Status: Note Saved Successfully.")

    @Slot()
    def names_inputs(self):
        name = self.student_name_line.text().strip()
        if name:
            self.save_button.setEnabled(True)
        else:
            self.save_button.setEnabled(False)
        
        if name:
            self.status_label.setText(f"Status: Typing name - {name}")
        else:
            self.status_label.setText("Status: Waiting for input")

    @Slot()
    def notes_inputs(self):

        note = self.notes_textbox.toPlainText()
        if note:
            self.save_button.setEnabled(True)
        else:
            self.save_button.setEnabled(False)
        
        if note:
            self.status_label.setText(f"Status: Note {note}")
        else:
            self.status_label.setText("Status: Waiting for input")
        
    @Slot()
    def clear_ui(self):
        self.student_name_line.setText("")
        self.notes_textbox.setText("")
        self.status_label.setText("Status: All Fields Cleared")
        self.save_button.setEnabled(False)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.resize(500, 500)
    
    window.show()
    sys.exit(app.exec_())