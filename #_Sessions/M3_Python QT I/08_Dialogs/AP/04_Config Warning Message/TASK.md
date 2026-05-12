## 🎯 AP. Config Warning Message

### **Task Objective**

**In this task, you will:**
* Create a PySide2 tool that displays a warning when a user attempts to overwrite an existing config file.
* Use `QMessageBox.warning()` to show a dialog with three response buttons: **Yes**, **No**, and **Cancel**.
* Display the result of the user’s decision in the interface.
* Simulate a common VFX workflow safeguard for protecting pipeline configuration files.


### **Instructions**

* Create a `QWidget`-based tool using PySide2.
* Add a button labeled **"Attempt Overwrite"**.
* When clicked:
  * Show a warning dialog titled **"Configuration Overwrite"**.
  * Include the message: **"A config file already exists. Overwrite it?"**
  * Provide three buttons: **Yes**, **No**, and **Cancel**.
* Display the selected response as feedback in a `QLabel` under the button:
  * If the user clicks **Yes**, show a message like: *"User chose to overwrite config."*
  * If **No**, show: *"User declined overwrite."*
  * If **Cancel**, show: *"User canceled the operation."*


### **Sample Output**

> For GUI Preview CHeckout :- output.gif

If the user clicks Yes:
```
User chose to overwrite config.
```
If the user clicks Cancel:
```
User canceled the operation.
```

