# Create a GUI for VFX Project Task Tracking

import sys

from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QListWidget,
                               QLineEdit, QCheckBox, QPushButton)


# def adding_new_task():
#     task_name_value = asset_task_name.text()
#     task_complete_status = asset_task_checkbox.isChecked()

#     # print(task_name_value, task_complete_status)

#     if not task_name_value:
#         status_message.addItem("Task name cannot be Empty.")
    
#     elif task_complete_status:
#         status_message.addItem(f"{task_name_value} - Completed")
#     else:
#         status_message.addItem(f"{task_name_value} - Not Completed")
        
# create application object  
app = QApplication(sys.argv)

# set window settings 
window = QWidget()
window.setWindowTitle("VFX Project Task Tracker")
window.resize(200, 120)

asset_task_name = QLineEdit()
asset_task_name.setPlaceholderText("Enter Task Name")

asset_task_checkbox  = QCheckBox("Task Completed")

aseet_task_button = QPushButton("Add Task")
status_message = QListWidget()

# Layout Setup
layout = QVBoxLayout()
layout.addWidget(asset_task_name)
layout.addWidget(asset_task_checkbox)
layout.addWidget(aseet_task_button)
layout.addWidget(status_message)

window.setLayout(layout)

# connect button
# aseet_task_button.clicked.connect(adding_new_task)

# display window
window.show()
sys.exit(app.exec_())