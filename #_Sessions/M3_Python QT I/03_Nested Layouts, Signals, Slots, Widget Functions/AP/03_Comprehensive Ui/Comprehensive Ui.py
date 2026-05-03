# Comprehensive UI

import sys

from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QSlider, QRadioButton, QCheckBox, QComboBox, QPushButton, QGroupBox

from PySide2.QtCore import Qt

app = QApplication()

window = QWidget()
window.setWindowTitle("Practice UI")

main_layout = QVBoxLayout()

header_label = QLabel("Enter Your Details:")
header_line = QLineEdit()
header_text = QTextEdit()
header_slider_label = QLabel("Slider Value: 20")
slider = QSlider(Qt.Horizontal)
slider.setMaximum(100)
slider.setMinimum(0)
slider.setValue(20)

def update_slider(value):
    header_slider_label.setText(f"Slider Value: {value}")

slider.valueChanged.connect(update_slider) # valuechanged is a signal gives out value as an int

# Group box creation
group_box = QGroupBox("Select Option")
radio_layout = QVBoxLayout()
radio1_btn = QRadioButton("Option 1")
radio2_btn = QRadioButton("Option 2")
radio3_btn = QRadioButton("Option 3")

radio_layout.addWidget(radio1_btn)
radio_layout.addWidget(radio2_btn)
radio_layout.addWidget(radio3_btn)
group_box.setLayout(radio_layout)

## checkbox creation

checkbox1 = QCheckBox("Checkbox1")
checkbox2 = QCheckBox("Checkbox2")

# Dropdown box creation

choice_drpDown = QComboBox()
choice_drpDown.addItems(["Choice 1","Choice 2","Choice 3"])

# submit button creation 
submit_btn = QPushButton("Submit")

def submit_btn_function():
    line_input = header_line.text()
    text_input = header_text.toPlainText()

    selected_radio = ""
    if radio1_btn.isChecked():
        selected_radio = "Option 1"
    elif radio2_btn.isChecked():
        selected_radio = "Option 2"
    elif radio3_btn.isChecked():
        selected_radio = "Option 3"

    selected_checkboxes = []
    if checkbox1.isChecked():
        selected_checkboxes.append("Checkbox 1")
    elif checkbox2.isChecked():
        selected_checkboxes.append("Checkbox 2")

    slider_value = slider.value()
    combo_value = choice_drpDown.currentText()

    # print the report 
    print(f"Text Input: {line_input}")
    print(f"Text Area: {text_input}")
    print(f"Selected Radio Button: {selected_radio}")
    print(f"Selected Checkboxes: {selected_checkboxes}")
    print(f"Slider Value: {slider_value}")
    print(f"Combobox Selection: {combo_value}")


main_layout.addWidget(header_label)
main_layout.addWidget(header_line)
main_layout.addWidget(header_text)
main_layout.addWidget(header_slider_label)
main_layout.addWidget(slider)
main_layout.addWidget(group_box)
# radio_layout.addWidget(radio1_btn)
main_layout.addWidget(checkbox1)
main_layout.addWidget(checkbox2)
main_layout.addWidget(choice_drpDown)
main_layout.addWidget(submit_btn)

window.setLayout(main_layout)

# submit button connection
submit_btn.clicked.connect(submit_btn_function)

window.show()
sys.exit(app.exec_())