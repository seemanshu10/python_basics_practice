import sys
from PySide2.QtWidgets import QApplication, QWidget, QComboBox

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox Example")

        combo = QComboBox(self)
        combo.addItems(["Option 1", "Option 2", "Option 3", "Option 4"])
        combo.move(30, 30)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.resize(200, 100)
    window.show()
    app.exec_()