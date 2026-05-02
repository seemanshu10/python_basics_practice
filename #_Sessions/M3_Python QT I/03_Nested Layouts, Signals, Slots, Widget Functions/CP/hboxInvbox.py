from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

app = QApplication()
window = QWidget()

vbox = QVBoxLayout()
hbox = QHBoxLayout()

hbox.addWidget(QPushButton('Button 1'))
hbox.addWidget(QPushButton('Button 2'))
vbox.addLayout(hbox)

hbox1 = QHBoxLayout()
hbox1.addWidget(QPushButton('Button 3'))
hbox1.addWidget(QPushButton('Button 4'))
vbox.addLayout(hbox1)

vbox.addWidget(QPushButton("Button 5"))
window.setLayout(vbox)

window.show()
app.exec_()