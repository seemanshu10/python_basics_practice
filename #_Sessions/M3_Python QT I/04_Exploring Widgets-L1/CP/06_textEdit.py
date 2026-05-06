import sys
from PySide2.QtWidgets import QApplication, QWidget, QTextEdit

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit Example")

        text_edit = QTextEdit(self)
        text_edit.setPlaceholderText("Enter multiple lines here")
        text_edit.setGeometry(20, 20, 100, 100)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.resize(250, 150)
    window.show()
    app.exec_()