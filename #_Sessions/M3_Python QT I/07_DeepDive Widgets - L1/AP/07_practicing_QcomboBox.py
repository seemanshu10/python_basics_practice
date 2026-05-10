import sys, os

from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox)

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
        self.setWindowTitle("Complete QComboBox Example")

        # Create widgets
        self.status_label = QLabel("Select a quality setting:")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setFont(QFont("Arial", 10))

        # Qcombobox 
        self.combo = QComboBox()
        self.combo.addItem("Low")   
        self.combo.addItems(["Medium", "High", "Ultra"])                             
        self.combo.setCurrentIndex(2)           
        
        # Buttons added
        self.print_button = QPushButton("Print Current Selection")
        self.clear_button = QPushButton("Clear Items")

        self.print_button.setStyleSheet("""
        QPushButton{
            background-color: green;
            border: 2px solid #888888;
            border-radius: 5px;
            color: #ffffff;
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

        self.clear_button.setStyleSheet("""
        QPushButton{
            background-color: green;
            border: 2px solid #888888;
            border-radius: 5px;
            color: #ffffff;
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

        # Connect signals
        
        self.print_button.clicked.connect(self.submit_text)
        self.clear_button.clicked.connect(self.clear_text)

        self.combo.activated.connect(self.activated_combo) # activated only by user interaction
        self.combo.highlighted.connect(self.highlight_combo)
        self.combo.currentIndexChanged.connect(self.current_index_combo)
        self.combo.currentTextChanged.connect(self.current_text_combo)
    
        # Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.status_label)
        main_layout.addWidget(self.combo)
        main_layout.addWidget(self.print_button)
        main_layout.addWidget(self.clear_button)

        self.setLayout(main_layout)

    # Signal callbacks
    def current_text_combo(self, state):
        self.status_label.setText(f"Current Selection: {state}")
        print(f"Text changed: {state}")

    def current_index_combo(self, state):
        self.status_label.setText(f"Current Index: {state}")
        print(f"Index changed: {state}")

    def highlight_combo(self):
        current_text = self.combo.currentText()
        self.status_label.setText(f"Highlight: {current_text}")
        print(f"Highlighted item: {current_text}")

    def activated_combo(self):
        current_text = self.combo.currentText()
        self.status_label.setText(f"Submitted: {current_text}")
        print(f"Activated item: {current_text}")

    # Button actions - slots 
    def submit_text(self):
        current_text = self.combo.currentText()
        self.status_label.setText(f"Submitted: {current_text}")
        print(f"Submitted: {current_text}")

    def clear_text(self):
        self.combo.clear()
        self.status_label.setText("All items cleared.")
        print("ComboBox cleared.")

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