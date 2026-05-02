from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

app = QApplication()
window = QWidget()

vbox = QVBoxLayout()  # Main vertical layout
hbox = QHBoxLayout()  # Nested horizontal layout

# Add buttons to horizontal layout
hbox.addWidget(QPushButton('Button 1'))
hbox.addWidget(QPushButton('Button 2'))

# Nest the horizontal layout inside the vertical layout

# Add another button directly to the vertical layout
vbox.addWidget(QPushButton('Button 3'))
vbox.addLayout(hbox)

# Apply layout to the window and show it
window.setLayout(vbox)
window.show()
app.exec_()