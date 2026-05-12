## 🎯 AP. Shot Type Dropdown

### **Task Objective**

**In this task, you will:**
* Build a PySide2 interface that allows users to select a shot type from a predefined list.
* Use `QInputDialog.getItem()` to display a dropdown menu.
* Store the selected item and display it in the interface.
* Simulate a tagging step in a VFX pipeline where shots are categorized by type.


### **Instructions**

* Create a QWidget-based interface using PySide2.
* Add a button labeled **"Pick Shot Category"**.
* When clicked:
  * Open a dropdown dialog with the following options:
    * `Plate`, `Comp`, `Matte Painting`, `Roto`, `Cleanup`
  * Set the first item (`Plate`) as the default.
  * Do not allow users to type in custom values — only select from the list.
* If a selection is confirmed:
  * Update a `QLabel` to display the selected item as:
    **"Selected shot type: [category]"**
* If the dialog is canceled, keep the label unchanged.


### **Sample Output**
> For GUI Preview CHeckout :- Output.gif

If the user selects:

```
Selected shot type: Comp
```

If canceled:

```
No shot type selected.
```
