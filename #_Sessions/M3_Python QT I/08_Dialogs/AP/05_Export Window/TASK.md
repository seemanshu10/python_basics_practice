## 🎯 AP. Export Window


### **Task Objective**

**In this task, you will:**
* Create a PySide2 tool that allows users to choose a save location for preview exports.
* Use `QFileDialog.getSaveFileName()` to open a save dialog with custom filters.
* Store and display the selected output path in the interface.
* Simulate a typical step in a VFX pipeline where artists export playblasts or review previews.

### **Instructions**

* Build a `QWidget`-based interface using PySide2.
* Add a button labeled **"Choose Save Location"**.
* When the button is clicked:
  * Open a file save dialog starting from the `/shots/` directory.
  * Allow users to save only `.mov` or `.mp4` files using a file filter.
* Display the selected save path in a `QLabel` under the button.
* If the user cancels the dialog, show a default message like “No file selected.”


### **Sample Output**

> For GUI Preview CHeckout :- output.png

```
Export path:
C:/project/seqA/shot010/preview_v01.mov
```

If canceled:

```
No file selected.
```
