from PySide2.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton
from PySide2.QtGui import QIcon
import sys

app = QApplication(sys.argv)

# Create the main window
window = QWidget()
layout = QVBoxLayout()

# Create QPushButton
button = QPushButton('Initial Button Text')
button.setText("New Button ")  # Changes the text on the button
button.setFixedSize(150, 50)  # Sets a fixed size for the button
button.setEnabled(True)  # Enables the button
button.setIcon(QIcon('path/to/icon.png'))  # Adds an icon (ensure path is correct)

# Function to handle button click
def clicked_button():
    print("Button Clicked")
    button.setText("Button 1")
    button.setEnabled(False)

# Connect button click to the function
button.clicked.connect(clicked_button)

# Add the button to the layout
layout.addWidget(button)
window.setLayout(layout)

# Function to print button details
def new():
    print(button)

# Show the window
window.show()

# Start the application
sys.exit(app.exec_())