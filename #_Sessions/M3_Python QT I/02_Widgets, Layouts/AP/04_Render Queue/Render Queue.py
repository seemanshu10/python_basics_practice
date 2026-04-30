# GUI to Monitor VFX Render Queue
# Create a GUI for VFX Project Task Tracking

import sys

from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QListWidget,
                               QLineEdit, QPushButton)

# create application object  
app = QApplication(sys.argv)

# set window settings 
window = QWidget()
window.setWindowTitle("VFX Render Queue")
window.resize(200, 120)

render_job_name_textbox = QLineEdit()
render_job_name_textbox.setPlaceholderText("Enter Job name")

asset_task_button = QPushButton("Add Job")
mark_complete_button = QPushButton("Mark Completed")
status_message_list = QListWidget()

# Layout Setup
layout = QVBoxLayout()
layout.addWidget(render_job_name_textbox)
layout.addWidget(asset_task_button)
layout.addWidget(mark_complete_button)
layout.addWidget(status_message_list)

window.setLayout(layout)

# connect button
# aseet_task_button.clicked.connect(adding_new_task)

# display window
window.show()
sys.exit(app.exec_())