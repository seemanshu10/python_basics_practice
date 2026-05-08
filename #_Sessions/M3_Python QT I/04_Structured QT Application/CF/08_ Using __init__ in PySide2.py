import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__() 
        self.initUI() 

    def initUI(self):
        # Adding a label to the window
        label = QLabel("Hello, PySide2!", self)
        self.setWindowTitle("My First Window") 
        self.resize(400, 300)

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MyWindow() 
    window.show() 
    sys.exit(app.exec_()) 