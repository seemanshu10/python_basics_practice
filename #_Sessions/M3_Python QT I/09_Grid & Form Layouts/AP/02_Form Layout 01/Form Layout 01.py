# Form Layout 01
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QFormLayout,
    QComboBox
)
import sys


class ContactForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(" Form Example")
        self.resize(650, 250)

        main_layout = QFormLayout(self)

        address_label = QLabel("Address: ")
        address_line = QLineEdit()

        city_label = QLabel("City: ")
        city_line = QLineEdit()

        state_label = QLabel("State: ")
        state_line = QComboBox()
        state_line.addItems(["Select State", "CA", "NY", "TX", "FL"])

        zip_label = QLabel("Zip: ")
        zip_line = QLineEdit()

        upb_label = QLabel("UPB: ")
        upb_line = QLineEdit()

        interest_label = QLabel("Interest Rate: ")
        interest_line = QLineEdit()

        pi_label = QLabel("P&I: ")
        pi_line = QLineEdit()

        term_label = QLabel("Term: ")
        term_line = QLineEdit()

        original_balance_label = QLabel("Original Balance: ")
        original_balance_line = QLineEdit()

        date_label = QLabel("Note Date: ")
        date_line = QLineEdit()

        last_paid_label = QLabel("Last Paid To: ")
        last_paid_line = QLineEdit()

        next_date_label = QLabel("Next Due Date: ")
        next_date_line = QLineEdit()

        maturity_date_label = QLabel("Maturity Date: ")
        maturity_date_line = QLineEdit()

        asset_label = QLabel("Asset Type: ")
        asset_line = QComboBox()
        asset_line.addItems(["Type 1", "Type 2", "Type 3"])
        
        note_label = QLabel("Asset Type: ")
        note_line = QComboBox()
        note_line.addItems(["Active", "Inactive", "Pending"])

        main_layout.addRow(address_label, address_line)
        main_layout.addRow(city_label, city_line)
        main_layout.addRow(state_label, state_line)
        main_layout.addRow(zip_label, zip_line)
        main_layout.addRow(upb_label, upb_line)
        main_layout.addRow(interest_label, interest_line)
        main_layout.addRow(pi_label, pi_line)
        main_layout.addRow(term_label, term_line)
        main_layout.addRow(original_balance_label, original_balance_line)
        main_layout.addRow(date_label, date_line)
        main_layout.addRow(last_paid_label, last_paid_line)
        main_layout.addRow(next_date_label, next_date_line)
        main_layout.addRow(maturity_date_label, maturity_date_line)
        main_layout.addRow(asset_label, asset_line)
        main_layout.addRow(note_label, note_line)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ContactForm()
    window.show()

    sys.exit(app.exec_())