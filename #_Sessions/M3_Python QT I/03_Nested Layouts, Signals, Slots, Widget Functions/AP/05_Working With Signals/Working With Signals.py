# Working with Signals

import sys

from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                               QPushButton, QLabel, QRadioButton, QLineEdit, QSlider, QCheckBox, QComboBox,QGroupBox, QTextEdit)

from PySide2.QtCore import Qt, Slot

@Slot()
def button_clicked():
    print("Button Clicked!")
@Slot()
def option_select():
    selected_options = ""
    if option1_rad_btn.isChecked():
        selected_options = "Option 1"
    elif option2_rad_btn.isChecked():
        selected_options = "Option 2"

    print(f"Option chose: {selected_options}")

@Slot()
def text_func():
    print(f"Text Entered: {line_text.text()}")

@Slot()
def update_slider(value):
    print("Slider Value Changed: ", value)

@Slot()
def combobox_selected():
    print(f"Preferred Contact: {combo_box.currentText()}")

@Slot()
def groupbox_selected(value):
    print(f"GroupBox Toggled: {value}")

@Slot()
def checkbox_selected():
    if checkbox.isChecked():
        print("Checkbox Checked")
    else:
        print("Checkbox Unchecked")

@Slot()
def textbox_word():
    text = text_box.toPlainText()
    word_count = len(text.split())

    print(f"Text Changed in QTextEdit. Word Count: {word_count}")


# define app
app = QApplication()

window = QWidget()
window.setWindowTitle("Working With Signals.")

main_layout = QVBoxLayout()
click_btn = QPushButton("Click Me")

# option_grp = QGroupBox()
option1_rad_btn = QRadioButton("Option1")
option2_rad_btn = QRadioButton("Option2")

label_name = QLabel("Type Something:")
line_text = QLineEdit()

slider = QSlider(Qt.Horizontal)

checkbox = QCheckBox("Check Me")

combo_box = QComboBox()
combo_box.addItems(["Item1", "Item2", "Item3"])

group_box = QGroupBox("Group Options")
group_box.setCheckable(True)

text_box = QTextEdit()

# main layout Creation
main_layout.addWidget(click_btn)
main_layout.addWidget(option1_rad_btn)
main_layout.addWidget(option2_rad_btn)
main_layout.addWidget(label_name)
main_layout.addWidget(line_text)
main_layout.addWidget(slider)
main_layout.addWidget(checkbox)
main_layout.addWidget(combo_box)
main_layout.addWidget(group_box)
main_layout.addWidget(text_box)

# signal connecting 
click_btn.clicked.connect(button_clicked)
option1_rad_btn.toggled.connect(option_select)
line_text.returnPressed.connect(text_func)
slider.valueChanged.connect(update_slider) # valuechanged is a signal
checkbox.stateChanged.connect(checkbox_selected)
combo_box.currentTextChanged.connect(combobox_selected)
group_box.clicked.connect(groupbox_selected)
text_box.textChanged.connect(textbox_word)


window.setLayout(main_layout)
window.show()
sys.exit(app.exec_())