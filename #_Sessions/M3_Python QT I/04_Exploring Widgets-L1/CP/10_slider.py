import sys
from PySide2.QtWidgets import QApplication, QWidget, QSlider
from PySide2.QtCore import Qt

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSlider Example")

        slider = QSlider(Qt.Horizontal, self)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(50)
        slider.move(20, 60)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.resize(300, 100)
    window.show()
    app.exec_()