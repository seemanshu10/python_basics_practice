from PySide2.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QLabel
)

app = QApplication([])
window = QWidget()
window.setWindowTitle("Shot Utility Panel")

# --- Main Vertical Layout ---
main_layout = QVBoxLayout()

# --- Header Row: Load Shot + Shot ID field ---
header_layout = QHBoxLayout()
load_btn = QPushButton("Load Shot")
shot_id_field = QLineEdit()
shot_id_field.setPlaceholderText("Enter Shot ID...")
header_layout.addWidget(load_btn)
header_layout.addWidget(shot_id_field)

# --- Action Row: Refresh + Update buttons ---
action_layout = QHBoxLayout()
refresh_btn = QPushButton("Refresh")
update_btn = QPushButton("Update")
action_layout.addWidget(refresh_btn)
action_layout.addWidget(update_btn)

# --- Export Section: Export buttons stacked vertically ---
export_layout = QVBoxLayout()
export_label = QLabel("Export Options:")
export_geo_btn = QPushButton("Export Geometry")
export_cam_btn = QPushButton("Export Camera")
export_layout.addWidget(export_label)
export_layout.addWidget(export_geo_btn)
export_layout.addWidget(export_cam_btn)

# --- Combine All Layouts ---
main_layout.addLayout(header_layout)
main_layout.addLayout(action_layout)
main_layout.addLayout(export_layout)

# Set main layout
window.setLayout(main_layout)
window.resize(300, 200)
window.show()
app.exec_()