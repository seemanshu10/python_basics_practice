import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Unstructured UI")
        self.setGeometry(100, 100, 300, 200)

        label = QLabel("This is an unstructured window", self)
        label.move(80, 60)

        button = QPushButton("Click Me", self)
        button.move(100, 100)
        button.clicked.connect(self.handle_click)

    def handle_click(self):
        print("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())