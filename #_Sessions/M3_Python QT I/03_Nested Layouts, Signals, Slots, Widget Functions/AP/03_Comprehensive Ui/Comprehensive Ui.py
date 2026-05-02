# Comprehensive UI

import sys

from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QSlider, QRadioButton, QCheckBox, QComboBox, QPushButton, QGroupBox

app = QApplication()

window = QWidget()
window.setWindowTitle("Practice UI")

main_layout = QVBoxLayout()

label_header_label = QLabel("Enter Your Details:")
label_header_line = QLineEdit()
label_header_text = QTextEdit()

main_layout.addWidget(label_header_label)
main_layout.addWidget(label_header_line)
main_layout.addWidget(label_header_text)

window.setLayout(main_layout)

window.show()
sys.exit(app.exec_())