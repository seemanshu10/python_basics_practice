## 🎯 **AP. Practice QInputDialog**

### Task Objective

By completing this task, you will:
* Use `QInputDialog` to collect user input in four different formats
* Trigger input prompts using `QPushButton`
* Display results in `QLineEdit` fields
* Use the dialog as an instance to access signal connections
* Apply basic styling to the dialog
* Use `exec_()` for modal behavior

### Instructions

You’re going to build a QWidget-based tool that collects different types of input using `QInputDialog`.
1. Create a window with vertical layout using `QVBoxLayout`.
2. Add 4 `QPushButton`s:
   * "Enter Name"
   * "Enter Frame Number"
   * "Enter Opacity"
   * "Select Render Engine"
3. Add 4 `QLineEdit` fields — each one should display the result of the corresponding input.
4. When each button is clicked, use the correct static method from `QInputDialog`:
   * `getText()` → for name input
   * `getInt()` → for frame number
   * `getDouble()` → for opacity
   * `getItem()` → for render engine selection (e.g., Arnold, Redshift, VRay)
5. Also create one **dialog instance** of `QInputDialog`:
   * Set the label text to "Enter Shot Number"
   * Connect these signals:
     * `textValueChanged` → print the current text
     * `textValueSelected` → print the final selected text
   * Apply this stylesheet:
     ```python
     dialog.setStyleSheet("QInputDialog { font-size: 14px; }")
     ```
   * Show the dialog using `exec_()`
* You can trigger the dialog instance using an extra button, like "Enter Shot Number".
* Make sure each input result appears in its matching `QLineEdit`.

### Sample Output
> Checkout output.gif for GUI Preview

**Console Output (Example for dialog instance):**
```
Changed: sh010
Changed: sh010b
Selected: sh010b
```
