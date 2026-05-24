## 🎯 AP. User Registration Form

### Task Objective

In this task, you will:

* Design a user registration form using Qt Designer.
* Use QGroupBox widgets to logically group related form fields.
* Organize widgets using vertical layouts for clean visual structure.
* Create a functional UI that includes input fields and checkboxes for user preferences.
* Set meaningful object names for all interactive widgets.

### Instructions

* Open Qt Designer and create a new Widget form.
* Add a QGroupBox titled "Personal Information":
  Inside this group box, add:
  * QLabel and QLineEdit for Name.
  * QLabel and QLineEdit for Email.
  * QLabel and QLineEdit for Password (set echoMode to Password).
  Apply a Vertical Layout inside the group box to stack the widgets.
* Add another QGroupBox titled "User Preferences":
  Inside this group box, add:
  * QCheckBox labeled "Subscribe to Newsletter".
  * QCheckBox labeled "Enable Notifications".
  Use a Vertical Layout for this group box as well.
* Add both QGroupBox widgets to the main form using a Vertical Layout.
* Add a QPushButton labeled "Submit" at the bottom of the form.
* Set the following object names for the widgets:
  * `lineEdit_name`
  * `lineEdit_email`
  * `lineEdit_password`
  * `checkBox_newsletter`
  * `checkBox_notifications`
  * `button_submit`
* Save the form as `user_registration_form.ui`.
* Preview the form to verify layout alignment and functionality.

### Sample Output

> Checkout output.png for GUI Preview

All fields should be vertically aligned and grouped logically in separate sections.
