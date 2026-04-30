# Asset Submission Form with Validation

import sys

from PySide2.QtWidgets import (QApplication, QWidget,
                               QVBoxLayout, QLineEdit, 
                               QComboBox, QPushButton,
                               QLabel)

def submit_asset_data():

    asset_name_value = asset_name_textbox.text()
    asset_type_value = asset_type_dropdown.currentText()
    # print(asset_name_value, asset_type_value)

    if not asset_name_value:
        status_message_label.setText("Error: Asset name cannot be empty.")
    elif asset_type_value == "Select Asset type":
        status_message_label.setText("Error: Please Select a valid asset type.")
    else:
        status_message_label.setText(f"Asset {asset_name_value} of type {asset_type_value} submitted successfully.")

# create application object  
app = QApplication(sys.argv)

# set wondow settings 
window = QWidget()
window.setWindowTitle("VFX Asset Submission")
window.resize(200, 120)

asset_name_textbox = QLineEdit()
asset_name_textbox.setPlaceholderText("Enter Asset Name")

asset_type_dropdown = QComboBox()
asset_type_dropdown.addItem("Enter Asset Type")
asset_type_dropdown.addItem("Texture")
asset_type_dropdown.addItem("Model")
asset_type_dropdown.addItem("Render")
asset_type_dropdown.setCurrentIndex(0) # no option is default 

submit_button = QPushButton("Submit")

status_message_label = QLabel()

# layout Setup 
layout = QVBoxLayout()
layout.addWidget(asset_name_textbox)
layout.addWidget(asset_type_dropdown)
layout.addWidget(submit_button)
layout.addWidget(status_message_label)

window.setLayout(layout)

# connect butoon
submit_button.clicked.connect(submit_asset_data)

# display window 
window.show()
sys.exit(app.exec_())