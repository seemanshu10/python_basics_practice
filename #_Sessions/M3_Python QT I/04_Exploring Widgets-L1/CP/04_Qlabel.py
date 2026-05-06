import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel Example ")

        label = QLabel("This is a QLabel", self)
        label.setGeometry(50, 30, 160, 40)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.resize(200, 100)
    window.show()
    app.exec_()