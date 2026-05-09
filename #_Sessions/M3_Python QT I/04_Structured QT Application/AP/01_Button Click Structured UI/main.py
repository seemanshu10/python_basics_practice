import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class MultiButtonGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi-Button PySide2 GUI")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Click a button below")
        layout.addWidget(self.label)

        self.button1 = QPushButton("Show Message 1")
        self.button1.clicked.connect(self.show_button1)
        layout.addWidget(self.button1)

        self.button2 = QPushButton("Show Message 2")
        self.button2.clicked.connect(self.show_button2)
        layout.addWidget(self.button2)

        self.setLayout(layout)

    def show_button1(self):
        self.label.setText("Hello! You clicked first button.")

    def show_button2(self):
        self.label.setText("Hello! You clicked second button.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    button = MultiButtonGUI()
    button.resize(200, 50)     
    button.show()                
    sys.exit(app.exec_())