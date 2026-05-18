import sys
from PySide2.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout Example")

        layout = QGridLayout()
        layout.addWidget(QPushButton("Top-Left"), 0, 0)
        layout.addWidget(QPushButton("Top-Right"), 0, 1)
        layout.addWidget(QPushButton("Bottom-Left"), 1, 0)
        layout.addWidget(QPushButton("Bottom-Right"), 1, 1)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.resize(250, 150)
    window.show()
    app.exec_()