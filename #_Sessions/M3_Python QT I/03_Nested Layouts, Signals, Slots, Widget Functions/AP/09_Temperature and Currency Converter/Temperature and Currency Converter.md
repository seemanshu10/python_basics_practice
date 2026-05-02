## 🎯 AP. Temperature and Currency Converter

### **Task Objective**
In this task, you will:
* Create a UI using `PySide2` that allows users to:
  * Convert temperature from Celsius to Fahrenheit.
  * Convert currency from USD to EUR.
* Implement real-time conversion using signals and slots.
* Use fixed exchange rate: **1 USD = 0.85 EUR**.

### **Instructions**
* Use `QWidget` as the main window.
* Set the layout to `QVBoxLayout`.
* Add the following sections:
#### Temperature Conversion:
* `QLabel`: “Celsius:”
* `QLineEdit`: for Celsius input.
* `QLabel`: “Fahrenheit:”
* `QLineEdit`: read-only field for Fahrenheit output.
* Connect the Celsius input field to a function that performs real-time conversion to Fahrenheit.
#### Currency Conversion:
* `QLabel`: “Amount in USD:”
* `QLineEdit`: for USD input.
* `QLabel`: “Equivalent in EUR:”
* `QLineEdit`: read-only field for EUR output.
* Connect the USD input field to a function that performs real-time conversion using the fixed rate.
* Align input text to the right using `.setAlignment(Qt.AlignRight)`.
