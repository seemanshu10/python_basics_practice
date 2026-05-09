import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel

import qdarkstyle

class WidgetStylingDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widget-specific Styling Demo") 
        self.setGeometry(300, 300, 400, 300)
        self.init_UI()

    def init_UI(self):
        self.apply_dark_theme()
        self.label = QLabel("Enter Your Name:", self)
        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(50, 50, 300, 40)
        self.line_edit.setPlaceholderText("Enter Text Here")
        
        self.button1 = QPushButton("Submit", self) 

        self.label.setGeometry(50, 70, 300, 40)
        self.line_edit.setGeometry(50, 120, 300, 40)
        self.button1.setGeometry(50, 180, 300, 40)
        
        self.button1.clicked.connect(self.on_button_clicked)

        self.button1.setStyleSheet("""
        QLineEdit{
            background-color: #f0f0f0;
            border-radius: 5px;
            }
        QPushButton{
            background-color: red;
            border-radius: 5px;
            color: white;
            padding: 10px;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #555555; 
        }
        """)

    def apply_dark_theme(self):
        dark_style_sheet = qdarkstyle.load_stylesheet_pyside2()
        self.setStyleSheet(dark_style_sheet)

    def on_button_clicked(self):
        print("Button Clicked!")

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = WidgetStylingDemo()
    window.show()

    sys.exit(app.exec_())