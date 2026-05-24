## 🎯 AP. Login Form

### Task Objective

In this task, you will:

* Design a login form using Qt Designer with grouped input fields and language selection.
* Use a QGroupBox to organize login-related inputs.
* Add a QComboBox to allow users to select their preferred language.
* Arrange all elements vertically using layout tools to ensure a clean and professional form structure.
* Assign appropriate object names for all key widgets.

### Instructions

* Open Qt Designer and create a new Widget form.
* Add a QGroupBox titled "Login Information".
  Inside the group box, add:
  * A QLabel and a QLineEdit for Username.
    Set object name: `lineEdit_username`
  * A QLabel and a QLineEdit for Password.
    Set object name: `lineEdit_password`
    Set `echoMode` property to Password
  Use a Vertical Layout inside the group box to align these inputs.
* Below the QGroupBox, add a QLabel with the text: "Select Language".
* Add a QComboBox directly below that label with the following items:
  * "English", "French", "Spanish"
    Set object name: `comboBox_language`
* Add a QPushButton below the combo box with the label "Login".
  Set object name: `button_login`
* Use a QVBoxLayout on the main form to arrange:
  * The Login Information group box
  * The Language selection label
  * The ComboBox
  * The Login button
* Save the form as `login_form_with_language.ui`.
* Preview the form to ensure everything is aligned and named correctly.

### Sample Output

> Checkout output.png for GUI Preview

```
[Window Title: Login Form]
┌────────────────────────────┐
│  Login Information         │
│  ───────────────────────   │
│  Username:    [**********] │
│  Password:    [**********] │ (Password-masked)
└────────────────────────────┘
Select Language:
[ English ▼ ]   ← QComboBox
[ Login ]       ← QPushButton
```