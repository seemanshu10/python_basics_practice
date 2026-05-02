from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

app = QApplication()

window = QWidget()

vbox = QVBoxLayout()
hbox = QHBoxLayout()

hbox.addWidget(QPushButton("Button 1"))
hbox.addWidget(QPushButton("Button 2"))

vbox.addLayout(hbox)
vbox.addWidget(QPushButton("Botton 2"))
vbox.addWidget(QPushButton("Botton 3"))

window.setLayout(vbox)

window.show()
app.exec_()