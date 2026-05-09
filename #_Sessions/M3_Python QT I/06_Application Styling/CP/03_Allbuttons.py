import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Global Styling Demo") 
        self.setGeometry(300, 300, 300, 250)
        self.init_ui()

    def init_ui(self):
    
        button1 = QPushButton("button 1", self) 
        button2 = QPushButton("button 2", self)
        button3 = QPushButton("button 3", self)

        button1.setGeometry(50, 50, 200, 40)
        button2.setGeometry(50, 100, 200, 40)
        button3.setGeometry(50, 150, 200, 40)
    
if __name__ == "__main__":

    app = QApplication(sys.argv)

    app.setStyleSheet("""
    QWidget{
            background-color: #2e2e20; 
            color: #ffffff;
            font-size: 14px;
    }
    QPushButton{
        background-color: #444444;
        border: 2px solid #888888;
        border-radius: 5px;
        color: #ffffff;
        padding: 10px;
        font-size: 14px;
    }
    QPushButton:hover {
        background-color: #555555; 
    }
    """)
    window = MyWindow()
    window.show()

    sys.exit(app.exec_())