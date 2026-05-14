from PySide2.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QLabel, QGridLayout, QVBoxLayout

from PySide2.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)
        # Initialize the form layout
        form_layout = QFormLayout()

        # Create widgets 
        self.username_label = QLabel("WWW:")
        self.username_input = QLineEdit()

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()

        # Add widgets 
        form_layout.addRow(self.username_label, self.username_input)
        form_layout.addRow(self.email_label, self.email_input)

        self.username_label.setAlignment(Qt.AlignBottom)
        self.email_label.setAlignment(Qt.AlignBottom)

        # add Details 
        details_layout = QGridLayout()

        lbl_street = QLabel("Street")
        self.edit_street = QLineEdit()

        lbl_apartment = QLabel("Apartment")
        self.edit_apartment = QLineEdit()

        lbl_postcode = QLabel("Post code")
        self.edit_postcode = QLineEdit()

        lbl_city = QLabel("City")
        self.edit_city = QLineEdit()

        lbl_country = QLabel("Country")
        self.edit_country = QLineEdit()

        details_layout.addWidget(lbl_street, 0, 0)
        details_layout.addWidget(self.edit_street, 0, 1)

        details_layout.addWidget(lbl_apartment, 0, 2)
        details_layout.addWidget(self.edit_apartment, 0, 3)

        details_layout.addWidget(lbl_postcode, 1, 0)
        details_layout.addWidget(self.edit_postcode, 1, 1)

        details_layout.addWidget(lbl_city, 1, 2)
        details_layout.addWidget(self.edit_city, 1, 3)

        details_layout.addWidget(lbl_country, 2, 0)
        details_layout.addWidget(self.edit_country, 2, 1, 1, 3)

        details_layout.setHorizontalSpacing(20)
        details_layout.setVerticalSpacing(15)

        main_layout.addLayout(details_layout)

        # form_layout.addRow()
        # Set the form layout to the window
        self.setLayout(form_layout)

if __name__ == "__main__":
    app = QApplication()

    window = MyWindow()
    window.resize(500, 200)
    window.show()

    app.exec_()