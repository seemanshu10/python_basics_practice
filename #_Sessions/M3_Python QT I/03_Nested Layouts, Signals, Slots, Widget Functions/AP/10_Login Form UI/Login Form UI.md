## 🎯 AP. Login Form UI 

### **Task Objective**
In this task, you will:
* Create a login form using PySide2.
* Add username and password input fields.
* Implement input validation using signals and slots.
* Enable the **Login** button **only when both fields are filled**.


### **Instructions**

#### Set up the Main Window
* Use `QWidget` as the main window container.
* Use `QVBoxLayout` to arrange all widgets vertically.
#### Add Username and Password Fields
* Add a `QLabel` and `QLineEdit` for **Username**.
* Add a `QLabel` and `QLineEdit` for **Password**.
  * Use `.setEchoMode(QLineEdit.Password)` to mask password input.
#### Add the Login Button
* Add a `QPushButton` labeled **Login**.
* Disable the button initially using `.setEnabled(False)`.
####  Implement Input Validation
* Use `.textChanged` signals on both fields.
* Connect to a slot (`validate_inputs`) that:
  * Enables the button **only if both username and password are non-empty**.
#### Run the Application
* Ensure the UI behaves as expected:
  * Button stays **disabled** until both fields have text.
  * Once both are filled, button becomes **enabled**.

### Sample Output
> Refer to Output.gif