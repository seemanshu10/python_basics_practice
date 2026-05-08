from PySide2. QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PySide2 Vertical Layout Example") 

layout = QVBoxLayout()

label = QLabel("Click the button to update this text.")
layout.addWidget(label)

button = QPushButton("Click Me")
button.setToolTip("This is a button!")
button.setEnabled(True)
layout.addWidget(button)

def on_button_clicked():
    label.setText("Button Clicked")

button.clicked.connect(on_button_clicked)

window.setLayout(layout)

window.show()
app.exec_()