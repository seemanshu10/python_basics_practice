from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
import sys

# Create the application instance
app = QApplication(sys.argv)

# Create the main window
window = QWidget()
window.setWindowTitle("PySide2 Vertical Layout Example")

# Create a layout
layout = QVBoxLayout()

# Create a label
label = QLabel("Click the button to update this text.")
layout.addWidget(label)

# Create a button
button = QPushButton("Click Me")
button.setToolTip("This is a button!")
button.setEnabled(True)
layout.addWidget(button)

# Define what happens when the button is clicked
def on_button_clicked():
    label.setText("Button clicked!")

# Connect the button's click to the function
button.clicked.connect(on_button_clicked)

# Apply the layout to the window
window.setLayout(layout)

# Show the window
window.show()

# Start the application event loop
app.exec_()