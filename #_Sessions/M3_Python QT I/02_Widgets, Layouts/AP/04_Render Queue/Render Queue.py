# GUI to Monitor VFX Render Queue

import sys

from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout,QListWidget,
                               QLineEdit, QPushButton, QListWidgetItem)

from PySide2.QtCore import Slot

@Slot()
def adding_new_job():
    task_name_value = render_job_name_textbox.text()

    if task_name_value:
        status_message_list.addItem(f"Job: {task_name_value} - In Progress")
        render_job_name_textbox.setText("")

@Slot()
def mark_selected_job():
    selected_job = status_message_list.selectedItems()

    for item in selected_job:
        job_text = item.text().replace(" - In Progress", "") # takes only job name 

        # Remove item
        row = status_message_list.row(item) # gives out row number  
        print(row)
        status_message_list.takeItem(row) # Delete the given row 

        # Add completed version
        completed_item = QListWidgetItem(f"{job_text} - Completed")
        status_message_list.addItem(completed_item)
    
# create application object  
app = QApplication(sys.argv)

# set window settings 
window = QWidget()
window.setWindowTitle("VFX Render Queue")
window.resize(500, 500)

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

asset_task_button.clicked.connect(adding_new_job)
mark_complete_button.clicked.connect(mark_selected_job)

# display window
window.show()
sys.exit(app.exec_())