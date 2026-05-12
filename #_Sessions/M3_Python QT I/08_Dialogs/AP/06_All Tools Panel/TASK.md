## 🎯 AP. Tool Configuration Panel

### **Task Objective**

**In this task, you will:**

* Build a configuration panel for collecting user-defined tool settings.
* Use built‑in Qt dialogs to gather folder paths, colors, notes, and font choices.
* Store and display user-selected configuration values inside the interface.
* Implement a confirmation step before applying the final settings.
* Simulate a real production tool used for configuring review and preview behavior in VFX pipelines.


### **Instructions**

* Create a **QWidget-based panel** using PySide2.
* Add the following buttons to the panel:
  * **Pick Folder**
  * **Choose Color**
  * **Enter Review Note**
  * **Choose Font**
  * **Confirm Settings**
* Each button must open its corresponding built‑in dialog and store the selected value internally.
* Display all current selections in a **QLabel** for continuous user feedback.
* When **Confirm Settings** is pressed:
  * Show a confirmation dialog asking whether the user wants to apply the settings.
  * If confirmed, display a final summary of all configuration values.
  * If canceled, display a message indicating the operation was canceled.

### **Sample Output (UI)**

> For GUI Preview CHeckout :- output.png

```
✅ Settings Applied:
Preview Folder: C:/Users/.../Screenshots
Note: Test 01
Color: #bc70ff
Font: Nirmala UI Semilight (18pt)
```

