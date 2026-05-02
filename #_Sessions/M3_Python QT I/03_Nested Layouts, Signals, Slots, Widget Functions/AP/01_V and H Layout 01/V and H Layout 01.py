# V & H Layout 01
import sys
from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                               QHBoxLayout, QPushButton, QCheckBox, 
                               QLabel, QLineEdit)

app = QApplication()

window = QWidget()
window.setWindowTitle("To Do List Example")

def create_rows_label_text(row_num):
    row = QHBoxLayout()
    row_num = QLabel(row_num)
    checkbox = QCheckBox()
    widget_text = QLineEdit()
    row.addWidget(row_num)
    row.addWidget(checkbox)
    row.addWidget(widget_text)
    return row

main_layout = QVBoxLayout()

for i in range (1,6):
    main_layout.addLayout(create_rows_label_text(f"{i}."))

button_layout = QHBoxLayout()
save_btn = QPushButton("Save")
exit_btn = QPushButton("Exit")

button_layout.addWidget(save_btn)
button_layout.addWidget(exit_btn)

main_layout.addLayout(button_layout)
window.setLayout(main_layout)

exit_btn.clicked.connect(window.close)

window.show()
sys.exit(app.exec_())
