## 🎯 AP. Comprehensive UI

### **Task Objective**

In this task, you will:
* Build a PySide2 GUI application that combines multiple common widgets in a single layout.
* Use widgets including: `QLabel`, `QLineEdit`, `QTextEdit`, `QSlider`, `QRadioButton`, `QCheckBox`, `QComboBox`, `QPushButton`, and `QGroupBox`.
* Organize the widgets using appropriate layout classes.
* Display a summary of all user inputs in the console when the Submit button is clicked.
* Update a label in real time to reflect the slider’s value.


### **Instructions**
* Check **Output.png** for UI Referece
* Create a main window using `QWidget` and set the title to **"Practice UI"**.
* Use `QVBoxLayout` as the main layout.
* Add the following widgets to the layout:
  * `QLabel` for instructions.
  * `QLineEdit` for single-line input.
  * `QTextEdit` for multi-line input.
  * `QSlider` (horizontal) and a label showing the slider's value.
  * A `QGroupBox` containing 3 `QRadioButton` widgets.
  * Two standalone `QCheckBox` widgets.
  * A `QComboBox` with at least three items.
  * A `QPushButton` labeled **"Submit"**.
* When the Submit button is clicked:
  * Collect and print all current values from the widgets to the console.

### **Sample Output**

* Output in Console

```text
Text Input: John Doe
Text Area: This is an example.
Selected Radio Button: Option 1
Selected Checkboxes: Checkbox 1, Checkbox 2
Slider Value: 45
ComboBox Selection: Choice 2
```
