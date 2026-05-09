import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class WidgetStylingDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widget-specific Styling Demo") 
        self.setGeometry(300, 300, 400, 300)
        self.init_UI()

    def init_UI(self):

        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(50, 50, 300, 40)
        self.line_edit.setPlaceholderText("Enter Text Here")
        
        button1 = QPushButton("Send", self) 
        button2 = QPushButton("Cancel", self)

        button1.setGeometry(50, 120, 300, 40)
        button2.setGeometry(50, 180, 300, 40)
        
        button2.setStyleSheet("""
        QLineEdit{
            background-color: #f0f0f0;
            border-radius: 5px;
            }
        QPushButton{
            background-color: #FF7522;
            border-radius: 5px;
            color: white;
            padding: 10px;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #555555; 
        }
        """)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = WidgetStylingDemo()
    window.show()

    sys.exit(app.exec_())