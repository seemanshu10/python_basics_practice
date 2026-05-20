import sys
from PySide2.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QPushButton, QComboBox

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFormLayout Example")

        layout = QFormLayout(self)
        layout.addRow("Name:", QLineEdit())                   # addRow(label, field)
        layout.addRow(QPushButton("Browse"))                  # addRow(widget only)
        layout.insertRow(0, "Email:", QLineEdit())            # insertRow
        layout.setSpacing(12)                                 # setSpacing
        layout.setContentsMargins(10, 10, 10, 10)              # setContentsMargins
        # layout.removeRow(1)      
        layout.addRow("Render Quality:", QComboBox())
        layout.addRow(QPushButton("Export"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.resize(300, 150)
    window.show()
    app.exec_()
