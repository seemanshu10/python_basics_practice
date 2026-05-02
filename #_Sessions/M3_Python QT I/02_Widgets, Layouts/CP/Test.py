import sys
from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QCheckBox, QSlider

from PySide2.QtCore import Qt

app = QApplication(sys.argv)
window = QWidget()

# Horizontal layout
# layout = QHBoxLayout()
# layout.addWidget(QLabel("New Label"))
# layout.addWidget(QPushButton("Button 1"))
# layout.addWidget(QPushButton("Button 2"))
# layout.addWidget(QPushButton("Button 3"))
# layout.addWidget(QSlider(Qt.Horizontal))


# window.setLayout(layout)

layout1 = QVBoxLayout()
# layout1.addLayout(layout)
layout1.addWidget(QLineEdit())
layout1.addWidget(QTextEdit())
layout1.addWidget(QPushButton("Click Me"))
layout1.addWidget(QCheckBox("Enable Feature"))
layout1.addWidget(QSlider(Qt.Horizontal))

window.setLayout(layout1)

window.show()
sys.exit(app.exec_())


