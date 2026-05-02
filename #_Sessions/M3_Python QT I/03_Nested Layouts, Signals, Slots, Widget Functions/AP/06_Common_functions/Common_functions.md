## 🎯 AP. Common_Functions

### **Task Objective**
In this task, you will:
* Build a PySide2 GUI application that demonstrates multiple **common widget functions**.
* Use `QLineEdit`, `QLabel`, `QCheckBox`, `QRadioButton`, and `QPushButton` in a functional form.
* Practice using widget behaviors such as `.setEnabled()`, `.setVisible()`, `.clear()`, `.setText()`, `.text()`, and `.setPlaceholderText()`.

### **Instructions**
* Refer Output.gif for Output Refereces
* Create a window titled **"Common Widget Functions"**.
* Add the following widgets:
  * A `QLineEdit` input field with a placeholder.
  * Two `QCheckBox` widgets:
    * One to **enable/disable** the input field.
    * One to **show/hide** the input field.
  * Two `QRadioButton` widgets:
    * One for **Uppercase**
    * One for **Lowercase**
  * Three `QPushButton` widgets:
    * **Clear** — clears the input field.
    * **Reset** — sets the input field to a preset value.
    * **Submit** — submits the current text to a label below.
  * A `QLabel` to display the **submitted result**.
* Organize all widgets using **`QVBoxLayout`** and **`QHBoxLayout`** as shown in the image.
* Implement the following widget functions:
  * Enable/Disable the input field based on checkbox state.
  * Show/Hide the input field based on checkbox state.
  * Transform the text to **uppercase or lowercase** depending on the selected radio button when submitting.
  * Display the submitted text dynamically below the buttons.


### **Sample Output Behavior**
* ✅ Checking “Enable Input” allows typing; unchecking disables it.
* ✅ Unchecking “Show Input” hides the input field.
* ✅ Clicking “Clear” empties the text field.
* ✅ Clicking “Reset” sets it to a predefined value.
* ✅ Selecting “Uppercase” or “Lowercase” changes text case on submission.
* ✅ Clicking “Submit” updates the label below with the processed text.

