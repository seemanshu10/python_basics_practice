# Temperature and Currency Converter

import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel
from PySide2.QtCore import Slot, Qt

@Slot()
def temperature_convertor():
    celsius_field = celsius_text.text()
    try:
        convert_temp = float(celsius_field)
        fahrenhiet_value = (convert_temp * 9 / 5) + 32
        fahrenheit_text.setText(f"{fahrenhiet_value:.2f}")

    except ValueError:
        celsius_text.clear()
        fahrenheit_text.clear()

@Slot()
def currency_convertor():
    amount_field = amount_usd_text.text()
    try:
        convert_currency = float(amount_field)
        currency_value = convert_currency * 0.85
        amount_eur_text.setText(f"{currency_value:.2f}")

    except ValueError:
        amount_usd_text.clear()
        amount_eur_text.clear()
    
app = QApplication()

window = QWidget()
window.setWindowTitle("Temperature and Currency Converter")

window.setFixedSize(400,250)

main_layout = QVBoxLayout()

# Temperature conversion
celsius_label = QLabel("Celsius:")
celsius_text = QLineEdit()
celsius_text.setAlignment(Qt.AlignRight)
celsius_text.setPlaceholderText("Enter Temperature in Celsius")


fahrenheit_label = QLabel("Fahrenheit:")
fahrenheit_text = QLineEdit()
fahrenheit_text.setAlignment(Qt.AlignRight)
fahrenheit_text.setReadOnly(True)
fahrenheit_text.setPlaceholderText("Temperature in Fahrenheit")

# connection signal 
celsius_text.textChanged.connect(temperature_convertor)

# currency convertor 
amount_usd_label = QLabel("Amount in USD:")
amount_usd_text = QLineEdit()
amount_usd_text.setAlignment(Qt.AlignRight)
amount_usd_text.setPlaceholderText("Enter Amount in USD")

amount_eur_label = QLabel("Equivalent in EUR:")
amount_eur_text = QLineEdit()
amount_eur_text.setAlignment(Qt.AlignRight)
amount_eur_text.setReadOnly(True)
amount_eur_text.setPlaceholderText("Convert to Euro")

# connection signal 
amount_usd_text.textChanged.connect(currency_convertor)

main_layout.addWidget(celsius_label)
main_layout.addWidget(celsius_text)
main_layout.addWidget(fahrenheit_label)
main_layout.addWidget(fahrenheit_text)

main_layout.addWidget(amount_usd_label)
main_layout.addWidget(amount_usd_text)
main_layout.addWidget(amount_eur_label)
main_layout.addWidget(amount_eur_text)

window.setLayout(main_layout)
window.show()
sys.exit(app.exec_())