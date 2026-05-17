## 🎯 AP. Practices QFormLayout

### Task Objective

By completing this task, you will:

* Use `QFormLayout` to design a vertical input form
* Add text fields and a combo box as form inputs
* Include a “Submit” button placed directly inside the form layout
* Display a status label below the form to show input feedback
* Connect user input (name field) to update the status label in real-time
* Apply basic custom styling to input widgets
* Combine `QFormLayout` with `QVBoxLayout` for main layout structure


### Instructions

* Create a `QWidget` window with a vertical layout
* Add a `QFormLayout` with:
  * A line edit labeled **Name**
  * A line edit labeled **Email**
  * A combo box labeled **Render Quality** with values: Low, Medium, High
  * A **Submit** button added as a single row (no label)
* Add a `QLabel` under the form to show status updates
* Connect the `textChanged` signal from the name input field to update the status label
* Set spacing and margins in the form layout
* Style both input fields with a dark theme and light text

### Sample Output

> Checkout output.gif

Behaviors:

* Typing in the **Name** field updates the status label in real time
* Inputs have custom styling applied (dark background, white text, border)
* Layout is vertically stacked with padding and clean spacing

