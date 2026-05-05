# Simple Quiz Application UI

import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QRadioButton
from PySide2.QtCore import Slot

@Slot()
def validate_answer():
    option1_rad_btn.setEnabled(False)
    option2_rad_btn.setEnabled(False)
    option3_rad_btn.setEnabled(False)
    option4_rad_btn.setEnabled(False)

    submit_btn.setEnabled(False)
    
    if option1_rad_btn.isChecked():
        if option1_rad_btn.text() == "Paris":
            answer_label.setText("Correct!")
    else:
        answer_label.setText("Incorrect!")

@Slot()
def reset_ui():
    option1_rad_btn.setEnabled(True)
    option2_rad_btn.setEnabled(True)
    option3_rad_btn.setEnabled(True)
    option4_rad_btn.setEnabled(True)
    submit_btn.setEnabled(True)

    answer_label.setText("")

app = QApplication()

window = QWidget()
window.setWindowTitle("Quix Application")

main_layout = QVBoxLayout()

quest_text = QLabel("What is the capital of France?")

option1_rad_btn = QRadioButton("Paris")
option2_rad_btn = QRadioButton("London")
option3_rad_btn = QRadioButton("Berlin")
option4_rad_btn = QRadioButton("Madrid")

submit_btn = QPushButton("Submit")
reset_btn = QPushButton("Reset")

answer_label = QLabel()

main_layout.addWidget(quest_text)
main_layout.addWidget(option1_rad_btn)
main_layout.addWidget(option2_rad_btn)
main_layout.addWidget(option3_rad_btn)
main_layout.addWidget(option4_rad_btn)

main_layout.addWidget(submit_btn)
main_layout.addWidget(reset_btn)

main_layout.addWidget(answer_label)

window.setLayout(main_layout)

# connection 
submit_btn.clicked.connect(validate_answer)
reset_btn.clicked.connect(reset_ui)

window.setFixedSize(300, 250)
window.show()

sys.exit(app.exec_())
