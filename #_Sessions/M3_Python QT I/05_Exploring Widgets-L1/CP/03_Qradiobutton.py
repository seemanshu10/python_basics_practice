import sys
from PySide2.QtWidgets import QApplication, QWidget, QRadioButton, QVBoxLayout

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QRadioButton Example ")
        
        layout = QVBoxLayout()

        radio1 = QRadioButton("Option 1 ")
        radio2 = QRadioButton("Option 2")

        layout.addWidget(radio1)
        layout.addWidget(radio2)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.resize(200, 100)
    window.show()
    app.exec_()