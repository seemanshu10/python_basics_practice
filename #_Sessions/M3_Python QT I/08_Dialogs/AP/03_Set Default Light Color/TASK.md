## 🎯 AP. Set Default Light Color 

### **Task Objective**

**In this task, you will:**

* Build a PySide2 tool that allows users to select a color for a default lighting setup.
* Use `QColorDialog.getColor()` to open a color picker dialog.
* Set a predefined initial color when the dialog opens.
* Apply the selected color to the text of a `QLabel` as visual feedback.
* Display the selected color’s HEX code in the label.


### **Instructions**

* Create a QWidget-based tool with PySide2.
* Add a button labeled **"Pick Light Color"**.
* When clicked:
  * Open a color picker dialog with an initial color set to white (`#ffffff`).
  * If the user selects a valid color:
    * Change the `QLabel` text to show: **"Light color set to: #hexvalue"**
    * Apply the selected color to the label’s text using a stylesheet.
  * If the user cancels the dialog, do not update the label.


### **Sample Output**

> For GUI Preview CHeckout :- Output.gif

If the user selects a color:
```
Light color set to: #ffcc00
```

And the label text appears in that color.
If canceled:
```
No color chosen.
```
