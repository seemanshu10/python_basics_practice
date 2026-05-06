import sys
from PySide2.QtWidgets import QApplication, QWidget, QLineEdit

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLineEdit Example")

        line_edit = QLineEdit(self)
        line_edit.setPlaceholderText("Enter text here")
        line_edit.move(20, 30)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.resize(250, 100)
    window.show()
    app.exec_()