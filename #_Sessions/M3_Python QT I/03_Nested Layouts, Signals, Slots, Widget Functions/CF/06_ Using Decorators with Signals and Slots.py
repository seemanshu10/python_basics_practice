from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

# Create the application
app = QApplication([])

# Create the main window
window = QWidget()
window.setWindowTitle("Using @Slot() Decorator")

# Set up the layout
layout = QVBoxLayout()

# Create a button
button = QPushButton("Click Me")

# Use the @Slot() decorator for the function
@Slot()
def say_hello():
    print("Button clicked, Hello!")

# Connect the button's clicked signal to the decorated function
button.clicked.connect(say_hello)

# Add the button to the layout
layout.addWidget(button)

# Set the layout for the window
window.setLayout(layout)
window.show()

# Run the application event loop
app.exec_()