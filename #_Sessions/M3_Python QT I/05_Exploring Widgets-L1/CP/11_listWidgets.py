import sys
from PySide2.QtWidgets import QApplication, QWidget, QListWidget

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListWidget Example")

        list_widget = QListWidget(self)
        list_widget.addItems(["Item 1", "Item 2", "Item 3"])
        list_widget.setGeometry(20, 20, 120, 80)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.resize(200, 150)
    window.show()
    app.exec_()