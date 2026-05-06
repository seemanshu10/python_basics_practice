import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPushButton Example")
        
        button = QPushButton("Click Me!", self)
        button.move(50, 50)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.resize(200, 150)
    window.show()
    
    app.exec_()