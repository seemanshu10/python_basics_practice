from PySide2.QtWidgets import (QApplication, QWidget, 
                               QVBoxLayout, QHBoxLayout, QLabel,
                               QLineEdit, QPushButton)

from PySide2.QtCore import Qt


app = QApplication()

window = QWidget()

main_layout = QVBoxLayout()
header_layout = QHBoxLayout()

machine_label = QLabel("Virtual Machine Name:")
machine_name = QLineEdit()
machine_name.setPlaceholderText("Enter Virtual Machine Name...")

create_vm_btn = QPushButton("Create VM")
create_vm_btn.setFixedSize(60, 20)

def crete_rows_label_text(label_text, widget):
    row = QHBoxLayout()
    label = QLabel(label_text)
    widget_text = QLineEdit(widget)
    row.addWidget(label)
    row.addWidget(widget_text, alignment = Qt.AlignCenter)
    return row

header_layout.addWidget(machine_label)
header_layout.addWidget(machine_name, alignment = Qt.AlignCenter)

tail_layout = QVBoxLayout()
tail_layout.addWidget(create_vm_btn, alignment = Qt.AlignCenter)

# all the fields creation 


# path_layout = QHBoxLayout()
# path_label = QLabel("VM Path")
# path_text = QLineEdit("D:")
# path_text.setPlaceholderText("Enter VM Path..")

# path_layout.addWidget(path_label)
# path_layout.addWidget(path_text, alignment = Qt.AlignCenter)

# boot_layout = QHBoxLayout()
# boot_label = QLabel("VM Booth DVD")
# boot_text = QLineEdit("F:/Deploy")
# boot_text.setPlaceholderText("Enter VM boot..")

# path_layout.addWidget(boot_label)
# path_layout.addWidget(boot_text, alignment = Qt.AlignCenter)

main_layout.addLayout(header_layout)
main_layout.addLayout(tail_layout)
# tail_layout.addLayout(path_layout)
# tail_layout.addLayout(boot_layout)

# adding Rows 
main_layout.addLayout(crete_rows_label_text("VM Path", "D:"))
main_layout.addLayout(crete_rows_label_text("VM Booth DVD", "F:/Deploy"))
main_layout.addLayout(crete_rows_label_text("VM Memory (Ex 2GB)", "2GB"))
main_layout.addLayout(crete_rows_label_text("VM VHDX Size (Ex 50GB)", "50GB"))
main_layout.addLayout(crete_rows_label_text("VM CPU Count", "2"))
main_layout.addLayout(crete_rows_label_text("VM Generation", "2"))
main_layout.addLayout(crete_rows_label_text("VM Network 1", "Internal 1"))
main_layout.addLayout(crete_rows_label_text("VM Network 2", "Internal 2"))

window.setLayout(main_layout)
window.resize(300,400)
window.show()

app.exec_()