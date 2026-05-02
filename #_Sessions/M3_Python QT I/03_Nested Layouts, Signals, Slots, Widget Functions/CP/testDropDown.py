from PySide2.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QVBoxLayout,QHBoxLayout, QPushButton
from PySide2.QtCore import Qt

app = QApplication()

window = QWidget()

window.setWindowTitle("Test")

main_layout = QVBoxLayout()

header_layout = QHBoxLayout()
application_label = QLabel("Select Application")
application_combo = QComboBox()
application_combo.addItems(["Script1", "Script2"])

header_layout.addWidget(application_label)
header_layout.addWidget(application_combo)

main_layout.addLayout(header_layout)

# launch_btn.
launch_btn = QPushButton("Launch")
main_layout.addWidget(launch_btn, alignment= Qt.AlignRight)

window.setLayout(main_layout)

window.show()
window.resize(200, 100)
app.exec_()