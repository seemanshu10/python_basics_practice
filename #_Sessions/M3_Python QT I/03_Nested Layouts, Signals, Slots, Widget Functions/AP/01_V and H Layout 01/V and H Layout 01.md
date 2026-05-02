## 🎯 AP. V & H Layout 01

### **Task Objective**

In this task, you will:
* Build a PySide2 GUI for a simple To-Do list interface using layout management.
* Use vertical and horizontal layouts to structure the interface.
* Create five rows of to-do items, each containing a checkbox, a numbered label, and a text field.
* Add two buttons (Save and Exit) aligned horizontally at the bottom.
* Implement an Exit button that closes the application.

### **Instructions**
* Create a window titled **"To Do List Example"**.
* Use a **QVBoxLayout** as the main layout of the application.
* For each of the five rows:
  * Use a **QHBoxLayout** to arrange a **QCheckBox**, a **QLabel** (numbered 1 to 5), and a **QLineEdit** horizontally.
  * Add each row layout to the main vertical layout.
* At the bottom, add a **QHBoxLayout** containing two **QPushButton** widgets: **"Save"** and **"Exit"**.
* Add this button layout to the main vertical layout.
* Connect the **Exit** button to close the application when clicked.

### **Sample Output**
> Refer Output.png for referece

*Note: The layout should clearly separate each row and place Save/Exit buttons horizontally beneath the list.*
