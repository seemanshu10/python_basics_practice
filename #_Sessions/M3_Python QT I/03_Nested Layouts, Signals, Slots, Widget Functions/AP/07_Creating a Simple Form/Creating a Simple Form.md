## 🎯 AP. Creating a Simple Form

### **Task Objective**

In this task, you will:
* Create a simple form using basic PySide2 widgets.
* Use vertical layout to organize the form elements.
* Handle a button click event using the signal-slot mechanism.
* Dynamically update a label based on user input.

### **Instructions**
* Create a main window using `QWidget`.
* Add the following widgets in a vertical layout:
  * A `QLabel` that prompts the user: **"Enter your name:"**
  * A `QLineEdit` for entering the name.
  * A `QPushButton` labeled **"Submit"**
* When the user clicks the **Submit** button, update the label to display:
  **"Hello, [name]!"**
* Set a fixed window size and an appropriate title for the application.


### **Sample Output (UI Preview)**
Before typing:

```
[Label] Enter your name:
[Text Field]
[Submit Button]
```
After entering `Alex` and clicking **Submit**:

```
[Label] Hello, Alex!
```