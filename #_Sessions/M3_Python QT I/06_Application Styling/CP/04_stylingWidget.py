import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class WidgetStylingDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widget Styling Demo") 
        self.setGeometry(300, 300, 300, 200)
        self.init_UI()

    def init_UI(self):

        
        button1 = QPushButton("Styled Button", self) 
        button2 = QPushButton("Default Button", self)

        button1.setGeometry(50, 50, 200, 40)
        button2.setGeometry(50, 100, 200, 40)
        
        button1.setStyleSheet("""
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
    window.resize(300, 200)
    window.show()

    sys.exit(app.exec_())