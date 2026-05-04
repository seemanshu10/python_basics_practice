# To-Do List Application UI
# Creating a Simple Form
import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout, QPushButton, QLineEdit, QListWidget, QLabel
from PySide2.QtCore import Slot

@Slot()
def submit_fields():
    text_field = name_text.text()
    print(text_field)
    name_list.addItem(f"{text_field}")

app = QApplication()

window = QWidget()
window.setWindowTitle("Sample Pyside2 UI")

window.setFixedSize(400,250)

main_layout = QVBoxLayout()

name_layout = QHBoxLayout()

name_label = QLabel("Enter Your Name:")
name_text = QLineEdit()
name_text.setPlaceholderText("Type Your name error.")

name_layout.addWidget(name_label)
name_layout.addWidget(name_text)

submit_btn = QPushButton("Add Name")

name_list = QListWidget()

# main_layout.addWidget(name_text)
main_layout.addLayout(name_layout)
main_layout.addWidget(submit_btn)
main_layout.addWidget(name_list)


# connection 
submit_btn.clicked.connect(submit_fields)

window.setLayout(main_layout)
window.show()
sys.exit(app.exec_())