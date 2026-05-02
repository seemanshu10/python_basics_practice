## 🎯 AP. V & H Layout 02

### **Task Objective**

In this task, you will:
* Build a PySide2 GUI layout that simulates a basic LDAP input form.
* Use vertical and horizontal layouts to structure input fields and buttons cleanly.
* Create labeled input fields for various user details.
* Align two buttons horizontally at the bottom of the window.
* Implement a Quit button that closes the application.


### **Instructions**
* Create a window titled **"LDAP Adder"**.
* Use a **QVBoxLayout** as the main layout to stack rows vertically.
* For each of the following fields, use a **QHBoxLayout**:
  * First name
  * Second name
  * Country (two letters)
  * City
  * Skype
* Each row must contain a **QLabel** on the left and a **QLineEdit** on the right.
* Add a final **QHBoxLayout** at the bottom containing two **QPushButton** widgets:
  * One labeled **"Show"**
  * One labeled **"Quit"**
* Connect the **Quit** button to close the application using `window.close()`.


### **Sample Output**
> Refer Output.png for referece
*Each row should be aligned horizontally, and all elements stacked vertically.*
