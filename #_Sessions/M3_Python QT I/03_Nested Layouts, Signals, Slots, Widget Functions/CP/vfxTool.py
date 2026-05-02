from PySide2.QtWidgets import (QApplication, QWidget, 
                               QVBoxLayout, QHBoxLayout, 
                               QPushButton, QLineEdit,
                               QLabel
)
app = QApplication()

window = QWidget()
window.setWindowTitle("Shot Utility Panel")

mainLayout = QVBoxLayout()

header_layout = QHBoxLayout()
load_btn = QPushButton("Load Shot")

shot_id_field = QLineEdit()
shot_id_field.setPlaceholderText("Enter Shot ID..")

header_layout.addWidget(load_btn)
header_layout.addWidget(shot_id_field)

button_layout = QHBoxLayout()

refresh_btn = QPushButton("Refresh")
update_btn = QPushButton("Update")

button_layout.addWidget(refresh_btn)
button_layout.addWidget(update_btn)


export_ver_layout = QVBoxLayout()

export_label = QLabel("Export Options:")
export_geo_btn = QPushButton("Export Geometry")
export_camera_btn = QPushButton("Export Camera")

export_ver_layout.addWidget(export_label)
export_ver_layout.addWidget(export_geo_btn)
export_ver_layout.addWidget(export_camera_btn)

mainLayout.addLayout(header_layout)
mainLayout.addLayout(button_layout)
mainLayout.addLayout(export_ver_layout)

window.setLayout(mainLayout)
window.resize(500, 200)

window.show()
app.exec_()