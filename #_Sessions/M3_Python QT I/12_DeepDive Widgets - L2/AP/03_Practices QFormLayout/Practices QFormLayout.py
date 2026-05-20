import sys
from PySide2.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton, QComboBox

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFormLayout Example")

        self.combo = QComboBox(self)
        self.combo.addItems(["Low", "Medium", "High"])

        layout = QFormLayout()
        layout.addRow("Name:", QLineEdit())
        layout.addRow("Email:", QLineEdit())
        layout.addRow("Render Quality:", self.combo)
        layout.addRow(QPushButton("Submit"))

        layout.setHorizontalSpacing(15)
        layout.setVerticalSpacing(20)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
    QLineEdit{
            background-color: #2e2e20; 
            color: #ffffff;
            font-size: 10px;
    }
    """)
    window = Main()
    window.resize(300, 150)
    window.show()
    app.exec_()