from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
import sys

# Create an application instance
app = QApplication(sys.argv)

# Create a main window using QWidget
window = QWidget()
window.setWindowTitle("PySide2 Vertical Layout Example")  

# Create a vertical layout
layout = QVBoxLayout()

# Create a label
label = QLabel("Click the button to update this text.")
layout.addWidget(label) 

# Create a button
button = QPushButton("Click Me")
button.setToolTip("This is a button!") 
button.setEnabled(True)  
layout.addWidget(button)  

# Define a slot function to handle button clicks
def on_button_clicked():
    label.setText("Button clicked!") 

button.clicked.connect(on_button_clicked)

window.setLayout(layout)
window.show()
app.exec_()
