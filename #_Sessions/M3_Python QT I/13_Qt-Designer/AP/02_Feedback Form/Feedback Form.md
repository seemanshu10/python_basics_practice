## 🎯 AP. Feedback Form

### Task Objective

In this task, you will:
* Design a feedback form using Qt Designer.
* Use QRadioButton widgets for a 1-to-5 rating system.
* Add a text field and submit button for user comments and form submission.
* Organize the radio buttons using a QGridLayout and use a QVBoxLayout to arrange the full form vertically.
* Assign clear and descriptive object names for all widgets.

### Instructions

* Open Qt Designer and create a new Widget form.
* Add a QLabel at the top of the form with the text: "Rate our Service".
* Below the label, add five QRadioButton widgets labeled "1" through "5".
* Use a QGridLayout to arrange the radio buttons in one row with five columns.
* Set their object names as:
  * `radioButton_1`
  * `radioButton_2`
  * `radioButton_3`
  * `radioButton_4`
  * `radioButton_5`
* Below the radio buttons, add another QLabel with the text: "Your Comments".
* Add a QLineEdit below the label for comment input.
* Set its object name to `lineEdit_comments`.
* Add a QPushButton at the bottom labeled "Submit Feedback".
* Set its object name to `button_submit`.
* Use a QVBoxLayout to stack:
  * The label for rating
  * The grid layout (with radio buttons)
  * The label for comments
  * The comment input field
  * The submit button
* Save the file as `feedback_form.ui`.
* Preview the form to ensure clean alignment and usability.

### Sample Output

> Checkout output.png for GUI Preview
