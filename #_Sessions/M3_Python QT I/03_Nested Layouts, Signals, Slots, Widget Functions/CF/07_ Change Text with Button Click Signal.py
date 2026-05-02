from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

# Create the application
app = QApplication([])

# Create the main window
window = QWidget()
window.setWindowTitle("Signal and Slot Example 1")

# Create widgets
label = QLabel("Initial Text")
button = QPushButton("Change Text")

# Set up the layout
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)
window.setLayout(layout)

# Define the slot function
def change_label_text():
    label.setText("Text Changed!")

# Connect the signal to the slot
button.clicked.connect(change_label_text)

# Show the window
window.show()

# Run the event loop
app.exec_()