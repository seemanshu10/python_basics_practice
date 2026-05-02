from PySide2.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton
from PySide2.QtGui import QIcon
import sys

app = QApplication(sys.argv)

window = QWidget()
layout = QVBoxLayout()

button = QPushButton("Initial Button Text")

button.setText("New Button")
button.setFixedSize(150, 50)
button.setEnabled(True)
# button.setIcon(QIcon(''))

def clicked_button():
    print("Button Clicked.")
    button.setText("Button 1")
    button.setEnabled(False)

button.clicked.connect(clicked_button)

layout.addWidget(button)
window.setLayout(layout)

def new():
    print(button)

window.show()
sys.exit(app.exec_)