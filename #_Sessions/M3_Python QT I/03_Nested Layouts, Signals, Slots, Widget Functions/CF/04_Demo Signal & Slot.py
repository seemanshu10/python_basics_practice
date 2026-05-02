from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PySide2.QtCore import Slot

# Create the application
app = QApplication([])

# Create the main window
window = QWidget()
window.setWindowTitle("Signal and Slot Demo")

# Create widgets
label = QLabel("Click the button below")
button = QPushButton("Click Me")

# Define the slot (response function)
@Slot()
def update_label():
    label.setText("Seemanshu clicked the button!")
    print("Button was clicked!")
    print("Seemanshu")

# Connect the signal to the slot
button.clicked.connect(update_label)
# button.triggered.connect(update_label)  # This will also trigger the slot when the button is triggered

# Set up the layout
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)

# Apply layout and show window
window.setLayout(layout)
window.resize(250, 120)
window.show()

# Run the event loop
app.exec_()
