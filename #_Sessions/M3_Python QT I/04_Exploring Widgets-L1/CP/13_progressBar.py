import sys
from PySide2.QtWidgets import QApplication, QWidget, QProgressBar

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressBar Example")

        progress = QProgressBar(self)
        progress.setMinimum(0)
        progress.setMaximum(100)
        progress.setValue(80)
        progress.setGeometry(20, 30, 200, 25)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.resize(250, 100)
    window.show()
    app.exec_()