import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Basic PySide2 App")
        self.setGeometry(100, 100, 300, 200)

        label = QLabel("Hello, World!", self)
        label.move(100, 80)

        button = QPushButton('Click Me', self)
        button.clicked.connect(self.button_click_handler)
        button.move(100, 120)

    def button_click_handler(self):
        print("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())