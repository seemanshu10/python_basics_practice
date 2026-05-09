import sys, os
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout
import qdarkstyle

class DarkModeDesignApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dark Mode App") 
        self.init_ui()

    def init_ui(self):
        self.apply_dark_theme()
        self.main_layout = QVBoxLayout()
        self.label = QLabel("Enter Text Click the button: ") 
        self.line_edit = QLineEdit()
        self.sumbit_btn = QPushButton("Click Me")

        self.line_edit.setPlaceholderText("Type Something...")

        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.line_edit)
        self.main_layout.addWidget(self.sumbit_btn)

        self.sumbit_btn.clicked.connect(self.on_button_click)

        self.setLayout(self.main_layout)

    def apply_dark_theme(self):
        dark_style_sheet = qdarkstyle.load_stylesheet_pyside2()
        self.setStyleSheet(dark_style_sheet)

    def on_button_click(self):

        entered_text = self.line_edit.text()
        self.label.setText(f"You Entered: {entered_text}")
    
if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = DarkModeDesignApp()
    window.resize(400, 150)
    window.show()

    sys.exit(app.exec_())