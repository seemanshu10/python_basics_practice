import sys, os

from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QRadioButton, QLineEdit)

from PySide2.QtCore import Qt, Slot
import qdarkstyle
from PySide2.QtGui import QFont

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):    
        # Window creating
        self.apply_dark_theme()
        self.setWindowTitle("Complete QLineEdit Example")
        self.resize(400, 250)

        # Create widgets
        self.status_label = QLabel("Enter filename:")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setFont(QFont("Arial", 10))

        self.line_edit = QLineEdit()

        self.line_edit.setText("Render_01")
        self.line_edit.setPlaceholderText("Enter output name")

        # setEchomode supports modes that allow the entered text to be suppressed or obscured
        self.line_edit.setEchoMode(QLineEdit.Normal)
        self.line_edit.setReadOnly(False)

        # # Styling
        self.line_edit.setStyleSheet("""
            QLineEdit {
                background-color: #2b2b2b;
                color: #f0f0f0;
                border: 2px solid #555;
                border-radius: 6px;
                padding: 8px;
                font-size: 14px;
            }

            QLineEdit:focus {
                border: 2px solid #4CAF50;
                background-color: #333333;
            }
        """)

        # Buttons added
        self.submit_button = QPushButton("Submit")
        self.submit_button.setStyleSheet("""
            QPushButton{
            background-color: Blue;
            border-radius: 5px;
            color: white;
            padding: 10px;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #555555; 
        }
        """)
        self.clear_button = QPushButton("Clear")

        # Connect signals
        self.line_edit.textChanged.connect(self.on_text_changed)
        self.line_edit.returnPressed.connect(self.on_return_pressed)
        self.line_edit.editingFinished.connect(self.on_editing_finished)

        self.submit_button.clicked.connect(self.submit_text)
        self.clear_button.clicked.connect(self.clear_text)

        # Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.status_label)
        main_layout.addWidget(self.line_edit)
        main_layout.addWidget(self.submit_button)
        main_layout.addWidget(self.clear_button)

        self.apply_stylesheet()    

        self.setLayout(main_layout)

    # Signal callbacks
    def on_text_changed(self, text):
        print(f"Text changed: {text}")

    def on_return_pressed(self):
        current_text = self.line_edit.text()
        print(f"Enter pressed. Current text: {current_text}")

    def on_editing_finished(self):
        current_text = self.line_edit.text()
        print(f"Editing finished: {current_text}")

    # Button actions
    def submit_text(self):
        current_text = self.line_edit.text()
        self.status_label.setText(f"Submitted: {current_text}")
        print(f"Submitted: {current_text}")

    def clear_text(self):
        self.line_edit.clear()
        self.status_label.setText("Input cleared.")

    def apply_stylesheet(self):

        stylesheet_path = os.path.dirname(os.path.abspath(__file__))

        stylesheet_path = os.path.join(stylesheet_path, "style.css")

        with open(stylesheet_path, "r") as f:
            style = f.read()
            self.setStyleSheet(style)

    @Slot()
    def apply_dark_theme(self):
        dark_style_sheet = qdarkstyle.load_stylesheet_pyside2()
        self.setStyleSheet(dark_style_sheet)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = Main()
    window.resize(400, 250)
    
    window.show()
    sys.exit(app.exec_())