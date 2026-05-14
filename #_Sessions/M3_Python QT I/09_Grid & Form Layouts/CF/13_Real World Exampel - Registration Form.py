from PySide2.QtWidgets import (
    QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QComboBox, 
    QCheckBox, QPushButton, QSpinBox, QVBoxLayout, QHBoxLayout
)
from PySide2.QtCore import Qt
class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        # Create a form layout
        form_layout = QFormLayout()

        # Name input
        self.name_input = QLineEdit()
        form_layout.addRow(QLabel("Full Name:"), self.name_input)

        # Email input
        self.email_input = QLineEdit()
        form_layout.addRow(QLabel("Email Address:"), self.email_input)

        # Age input (using QSpinBox for numerical input)
        self.age_input = QSpinBox()
        self.age_input.setRange(0, 100)  # Set age range from 0 to 100
        form_layout.addRow(QLabel("Age:"), self.age_input)

        # Gender selection (using QComboBox)
        self.gender_input = QComboBox()
        self.gender_input.addItems(["Select", "Male", "Female", "Other"])
        form_layout.addRow(QLabel("Gender:"), self.gender_input)

        # Newsletter subscription (using QCheckBox)
        self.newsletter_checkbox = QCheckBox("Subscribe to Newsletter")
        form_layout.addRow(self.newsletter_checkbox)

        # Terms and Conditions (using QCheckBox)
        self.terms_checkbox = QCheckBox("I agree to the Terms and Conditions")
        form_layout.addRow(self.terms_checkbox)

        # Submit and Cancel buttons (QPushButton)
        button_layout = QHBoxLayout()  # Create horizontal layout for buttons
        self.submit_button = QPushButton("Submit")
        self.cancel_button = QPushButton("Cancel")
        self.ok_button = QPushButton("OK")
        button_layout.addWidget(self.submit_button)
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.ok_button)

        # Add the button layout to the form
        form_layout.addRow(button_layout)

        # Set layout
        self.setLayout(form_layout)

        # Signals for button actions
        self.submit_button.clicked.connect(self.submit_form)
        self.cancel_button.clicked.connect(self.clear_form)

    def submit_form(self):
        # Gather all input data and print (or process further)
        name = self.name_input.text()
        email = self.email_input.text()
        age = self.age_input.value()
        gender = self.gender_input.currentText()
        newsletter = self.newsletter_checkbox.isChecked()
        terms = self.terms_checkbox.isChecked()
        if not terms:
            print("Please agree to the Terms and Conditions!")
            return
        
        # Print form data (replace with actual form submission logic)
        print(f"Name: {name}\nEmail: {email}\nAge: {age}\nGender: {gender}\n"
              f"Subscribed to Newsletter: {newsletter}\nAgreed to Terms: {terms}")
        
    def clear_form(self):
        # Clear all fields
        self.name_input.clear()
        self.email_input.clear()
        self.age_input.setValue(0)
        self.gender_input.setCurrentIndex(0)
        self.newsletter_checkbox.setChecked(False)
        self.terms_checkbox.setChecked(False)

if __name__ =="__main__":
    # Run the application
    app = QApplication([])
    window = RegistrationForm()
    window.setWindowTitle("Advanced User Registration Form")
    window.show()
    app.exec_()