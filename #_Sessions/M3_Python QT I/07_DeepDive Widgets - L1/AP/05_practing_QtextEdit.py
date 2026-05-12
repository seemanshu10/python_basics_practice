import sys, os

from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit)

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
        self.setWindowTitle("Complete QTextEdit Example")

        # Create widgets
        self.status_label = QLabel("Render Log Area:")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setFont(QFont("Arial", 10))

        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Log messages appear here...")
        self.text_edit.setReadOnly(False)

        # # Styling
        self.text_edit.setStyleSheet("""
            QTextEdit {
                background-color: #2b2b2b;
                color: #f0f0f0;
                border: 2px solid #555;
                border-radius: 6px;
                padding: 8px;
                font-size: 14px;
            }

            QTextEdit:focus {
                border: 2px solid #4CAF50;
                background-color: #333333;
            }
        """)

        # Buttons added
        self.print_plain_button = QPushButton("Print Plain Text")
        self.print_plain_button.setStyleSheet("""
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
        QPushButton:pressed {
            background-color: #b91f1f;
            border: 2px solid #ffffff;
        }                                      
        """)
        self.print_html_button = QPushButton("Print HTML Text")
        self.clear_button = QPushButton("Clear Text")
        self.toggled_read_button = QPushButton("Toggled Read Only")

        # Connect signals
        self.text_edit.textChanged.connect(self.on_text_changed)
        
        self.print_plain_button.clicked.connect(self.submit_text)
        self.print_html_button.clicked.connect(self.submit_tohtml)
        self.clear_button.clicked.connect(self.clear_text)
        self.toggled_read_button.clicked.connect(self.on_toggled_read_button)

        # Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.status_label)
        main_layout.addWidget(self.text_edit)
        main_layout.addWidget(self.print_plain_button)
        main_layout.addWidget(self.print_html_button)
        main_layout.addWidget(self.clear_button)
        main_layout.addWidget(self.toggled_read_button)

        self.apply_stylesheet()    

        self.setLayout(main_layout)

    # Signal callbacks
    def on_text_changed(self):
        text = self.text_edit.toPlainText()
        print(f"Text changed: {text}")

    def on_toggled_read_button(self):
        current_state = self.text_edit.isReadOnly()

        self.text_edit.setReadOnly(not current_state)

        # Update label
        if self.text_edit.isReadOnly():
            self.status_label.setText("Log Area is now READ ONLY")
            print(f"Status Changed: {current_state}")
        else:
            self.status_label.setText("Log Area is now EDITABLE")
            print(f"Status Changed: {current_state}")

    # Button actions - slots 
    def submit_text(self):
        current_text = self.text_edit.toPlainText()
        self.status_label.setText(f"Submitted: {current_text}")
        print(f"Submitted: {current_text}")

    def submit_tohtml(self):
        current_text = self.text_edit.toHtml()
        self.status_label.setText(f"Submitted: {current_text}")
        print(f"Submitted: {current_text}")

    def clear_text(self):
        self.text_edit.clear()
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
    window.resize(500, 350)
    
    window.show()
    sys.exit(app.exec_())