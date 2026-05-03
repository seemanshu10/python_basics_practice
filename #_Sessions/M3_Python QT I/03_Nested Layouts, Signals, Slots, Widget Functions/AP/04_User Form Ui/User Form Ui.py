# User Form UI
import sys

from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout,QVBoxLayout, QLabel, QLineEdit, QTextEdit, QSlider, QRadioButton, QCheckBox, QComboBox, QPushButton, QGroupBox

from PySide2.QtCore import Qt, Slot

def update_slider(value):
    rating_label.setText(f"Rating: {value}")

def summary_report():

    # Summary Report 
    print(f"{first_name_label.text()} {first_name_text.text()}")
    print(f"{last_name_label.text()} {last_name_text.text()}")

    selected_gender = ""
    if male_rad_btn.isChecked():
        selected_gender = "Male"
    elif female_rad_btn.isChecked():
        selected_gender = "Female"
    elif other_rad_btn.isChecked():
        selected_gender = "Other"

    print(f"{gender_label.text()} {selected_gender}")

    selected_intrests = []
    if music_chekbox_btn.isChecked():
        selected_intrests.append("Music")
    if sport_chekbox_btn.isChecked():
        selected_intrests.append("Sports")
    if reading_chekbox_btn.isChecked():
        selected_intrests.append("Reading")

    if selected_intrests == []:
        print(f"{intrest_label.text()} None")
    else:    
        print(f"{intrest_label.text()} {', '.join(selected_intrests)}")

    print(f"Feeback: {comments_text.toPlainText()}")
    print(f"Rating : {slider.value()}")
    print(f"Preferred Contact: {contact_combo.currentText()}")

app = QApplication()

window = QWidget()
window.setWindowTitle("Advanced User Form")

main_layout = QVBoxLayout()
head_label = QLabel("User Feedback Form")

# name layout 
name_layout = QHBoxLayout()
first_name_label = QLabel("First Name: ")
first_name_text = QLineEdit()

last_name_label = QLabel("Last Name: ")
last_name_text = QLineEdit()

name_layout.addWidget(first_name_label)
name_layout.addWidget(first_name_text)
name_layout.addWidget(last_name_label)
name_layout.addWidget(last_name_text)

# Gender layout 
gender_layout = QHBoxLayout()
gender_label = QLabel("Gender:")

male_rad_btn = QRadioButton()
male_rad_label = QLabel("Male")

female_rad_btn = QRadioButton()
female_rad_label = QLabel("Female")

other_rad_btn = QRadioButton()
other_rad_label = QLabel("Other")

gender_layout.addWidget(gender_label)
gender_layout.addWidget(male_rad_btn, alignment= Qt.AlignRight)
gender_layout.addWidget(male_rad_label, alignment= Qt.AlignLeft)
gender_layout.addWidget(female_rad_btn, alignment= Qt.AlignRight)
gender_layout.addWidget(female_rad_label, alignment= Qt.AlignLeft)
gender_layout.addWidget(other_rad_btn, alignment= Qt.AlignRight)
gender_layout.addWidget(other_rad_label, alignment= Qt.AlignLeft)

# Intrests Layout 
intrest_layout = QHBoxLayout()
intrest_label = QLabel("Intrests:")

music_chekbox_btn = QCheckBox()
music_chekbox_label = QLabel("Music")

sport_chekbox_btn = QCheckBox()
sport_chekbox_label = QLabel("Sport")

reading_chekbox_btn = QCheckBox()
reading_chekbox_label = QLabel("Reading")

intrest_layout.addWidget(intrest_label)
intrest_layout.addWidget(music_chekbox_btn, alignment= Qt.AlignRight)
intrest_layout.addWidget(music_chekbox_label, alignment= Qt.AlignLeft)
intrest_layout.addWidget(sport_chekbox_btn, alignment= Qt.AlignRight)
intrest_layout.addWidget(sport_chekbox_label, alignment= Qt.AlignLeft)
intrest_layout.addWidget(reading_chekbox_btn, alignment= Qt.AlignRight)
intrest_layout.addWidget(reading_chekbox_label, alignment= Qt.AlignLeft)

# rating Layout 
rating_layout = QHBoxLayout()

rating_slider_label = QLabel("Rating (1-10):")
slider = QSlider(Qt.Horizontal)
rating_label = QLabel("Rating: 1")
slider.setMaximum(10)
slider.setMinimum(1)
slider.setValue(1)


slider.valueChanged.connect(update_slider) # valuechanged is a signal 

rating_layout.addWidget(rating_slider_label)
rating_layout.addWidget(slider)
rating_layout.addWidget(rating_label)

# contact Layout 
contact_layout = QHBoxLayout()
contact_label = QLabel("Preferred Contact Method: ")
contact_combo = QComboBox()
contact_combo.addItems(["Phone", "Email", "SMS"])

contact_layout.addWidget(contact_label)
contact_layout.addWidget(contact_combo)

# Submit Button 
submit_btn = QPushButton("Submit")

# Summary Layout
summary_label = QLabel("Summary of Input:")
summary_text = QTextEdit()

# main Layout Start 
main_layout.addWidget(head_label, alignment= Qt.AlignCenter)
main_layout.addLayout(name_layout)
main_layout.addLayout(gender_layout)
main_layout.addLayout(intrest_layout)
# Comments/ Feedback:
comments_label = QLabel("Comments/Feedback:")
comments_text = QTextEdit()

main_layout.addWidget(comments_label)
main_layout.addWidget(comments_text)
main_layout.addLayout(rating_layout)
main_layout.addLayout(contact_layout)

main_layout.addWidget(submit_btn)
main_layout.addWidget(summary_label)
main_layout.addWidget(summary_text)

window.setLayout(main_layout)

submit_btn.clicked.connect(summary_report)

window.show()
sys.exit(app.exec_())