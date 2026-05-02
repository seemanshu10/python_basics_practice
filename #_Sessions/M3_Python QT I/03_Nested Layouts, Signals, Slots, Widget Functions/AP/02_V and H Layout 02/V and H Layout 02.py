# V & H Layout 02
import sys

from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout, QLabel, QLineEdit, QPushButton

from PySide2.QtCore import Slot
app = QApplication()

window = QWidget()
window.setWindowTitle("LDAP Adder")

@Slot
def create_rows_label_text(label_text):
    row = QHBoxLayout()
    row_label = QLabel(label_text)
    widget_text = QLineEdit()
    row.addWidget(row_label)
    row.addWidget(widget_text)
    return row

main_layout = QVBoxLayout()

main_layout.addLayout(create_rows_label_text("First Name"))
main_layout.addLayout(create_rows_label_text("Second Name"))
main_layout.addLayout(create_rows_label_text("Country (Two Letters)"))
main_layout.addLayout(create_rows_label_text("City"))
main_layout.addLayout(create_rows_label_text("Skype"))

button_layout = QHBoxLayout()
show_btn = QPushButton("Show")
quit_btn = QPushButton("Quit")

button_layout.addWidget(show_btn)
button_layout.addWidget(quit_btn)

main_layout.addLayout(button_layout)

window.setLayout(main_layout)

# button connection exit 
quit_btn.clicked.connect(window.close)

window.show()

sys.exit(app.exec_())