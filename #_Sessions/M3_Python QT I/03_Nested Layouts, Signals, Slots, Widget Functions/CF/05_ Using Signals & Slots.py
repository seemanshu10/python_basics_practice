from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

# Create the application
app = QApplication([])

# Create the main window
window = QWidget()
window.setWindowTitle("Button Click Signal Example")

# Set up the layout
layout = QVBoxLayout()

# Create a button
button = QPushButton("Click Me")

# Define the slot function to handle the button click signal
def on_button_clicked():
    print("Button was clicked!")

# Connect the button's clicked signal to the slot function
button.clicked.connect(on_button_clicked)

# Add the button to the layout
layout.addWidget(button)

# Set the layout for the window
window.setLayout(layout)
window.show()

# Run the application event loop
app.exec_()