from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

app = QApplication([])
window = QWidget()

# Create the main horizontal layout
hbox = QHBoxLayout()

# First vertical layout (left column)
vbox1 = QVBoxLayout()
vbox1.addWidget(QPushButton('Button 1'))
vbox1.addWidget(QPushButton('Button 2'))

# Second vertical layout (right column)
vbox2 = QVBoxLayout()
vbox2.addWidget(QPushButton('Button 3'))
vbox2.addWidget(QPushButton('Button 4'))

# Add both vertical layouts to the horizontal layout
hbox.addLayout(vbox1)
hbox.addLayout(vbox2)

# Set layout on the window and display it
window.setLayout(hbox)
window.show()
app.exec_()