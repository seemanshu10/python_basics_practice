import sys
from PySide2.QtWidgets import QApplication, QWidget, QGroupBox, QVBoxLayout, QRadioButton

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGroupBox Example")

        group_box = QGroupBox("Choose an Option", self)
        layout = QVBoxLayout()
        layout.addWidget(QRadioButton("Option 1"))
        layout.addWidget(QRadioButton("Option 2"))
        group_box.setLayout(layout)
        group_box.move(20, 20)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.resize(250, 150)
    window.show()
    app.exec_()