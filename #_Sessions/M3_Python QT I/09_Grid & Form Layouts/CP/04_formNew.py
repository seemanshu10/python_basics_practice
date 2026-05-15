from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QGridLayout,
    QVBoxLayout,
    QFrame,
)
import sys


class ContactForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contact Form")
        self.resize(650, 250)

        main_layout = QVBoxLayout(self)

        # Top section
        top_layout = QGridLayout()

        lbl_www = QLabel("WWW")
        self.edit_www = QLineEdit()

        lbl_email = QLabel("E-mail")
        self.edit_email = QLineEdit()

        top_layout.addWidget(lbl_www, 0, 0)
        top_layout.addWidget(self.edit_www, 0, 1)

        top_layout.addWidget(lbl_email, 1, 0)
        top_layout.addWidget(self.edit_email, 1, 1)

        main_layout.addLayout(top_layout)

        # Details label
        details_label = QLabel("Details")
        details_label.setStyleSheet("font-weight: bold;")
        main_layout.addWidget(details_label)

        # Details form
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
        details_layout.addWidget(self.edit_city,1, 3)

        details_layout.addWidget(lbl_country, 2, 0)
        details_layout.addWidget(self.edit_country, 2, 1,1, 3)

        details_layout.setHorizontalSpacing(20)
        details_layout.setVerticalSpacing(15)

        main_layout.addLayout(details_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ContactForm()
    window.show()

    sys.exit(app.exec_())