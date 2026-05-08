import sys
from PySide2.QtWidgets import QApplication, QWidget, QCheckBox

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCheckBox Example")

        check_box = QCheckBox("Check!", self)
        check_box.move(30, 30)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.resize(200, 100)
    window.show()
    app.exec_()