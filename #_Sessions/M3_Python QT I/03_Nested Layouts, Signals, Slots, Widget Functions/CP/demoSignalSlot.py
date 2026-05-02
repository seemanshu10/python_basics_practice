from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

from PySide2.QtCore import Slot

app = QApplication()

window = QWidget()
window.setWindowTitle("Signal and Slot Demo")

label = QLabel("Click the button Below")
button = QPushButton("Click Me")

@Slot()
def update_label():
    print("Button was clicked!")
    label.setText("You Clicked the button!")

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)

window.setLayout(layout)

button.clicked.connect(update_label)
window.resize(250, 120)
window.show()

app.exec_()
