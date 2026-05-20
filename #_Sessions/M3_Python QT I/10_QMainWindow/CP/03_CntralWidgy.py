from PySide2.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout ,QPushButton, 
    QGridLayout
)

import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMAin WIndow Example")

        self.setGeometry(300, 300, 400, 200)

        self.central_widget = QWidget()

        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(QPushButton("Button 1"))
        self.main_layout.addWidget(QPushButton("Button 2"))

        # Horizontal 
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.addWidget(QPushButton("Button 3"))
        self.horizontal_layout.addWidget(QPushButton("Button 4"))

        # Grid LAyout 
        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(QPushButton("Button 6"), 0,0)
        self.grid_layout.addWidget(QPushButton("Button 7"), 0, 1)
        self.grid_layout.addWidget(QPushButton("Button 8"), 1, 0)
        self.grid_layout.addWidget(QPushButton("Button 9"), 1, 1)

        self.main_layout.addLayout(self.horizontal_layout)
        self.main_layout.addLayout(self.grid_layout)

        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)


if __name__ == "__main__":

    app = QApplication()
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())

