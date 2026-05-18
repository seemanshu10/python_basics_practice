import sys
from PySide2.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFormLayout Example")

        layout = QFormLayout()
        layout.addRow("Name:", QLineEdit())
        layout.addRow("Department:", QLineEdit())
        layout.addRow("Version:", QLineEdit())
        layout.addRow(QPushButton("Submit"))

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.resize(300, 150)
    window.show()
    app.exec_()
