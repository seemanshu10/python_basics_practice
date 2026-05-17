## 🎯 **AP. Practice QMessageBox**

### Task Objective

By completing this task, you will:
* Create a message box using `QMessageBox`
* Set its main text, informative text, icon, buttons, and default button
* Connect the `buttonClicked` signal to a handler
* Style the message box using `setStyleSheet`
* Use the return value of `exec_()` to control logic
* Integrate the message box with a `QPushButton` inside a basic window layout

### Instructions

Create a PySide2 UI that shows a message box when a button is clicked.
1. Create a `QWidget` window with a `QVBoxLayout`.
2. Add a `QPushButton` labeled **“Delete Render Cache”**.
3. When the button is clicked, show a `QMessageBox` instance (not static).
   Configure the message box using these:
   * `setText("Delete render cache?")`
   * `setInformativeText("This action cannot be undone.")`
   * `setIcon(QMessageBox.Warning)`
   * `setStandardButtons(QMessageBox.Yes | QMessageBox.No)`
   * `setDefaultButton(QMessageBox.No)`
4. Add this style to the message box:
   ```python
   msg.setStyleSheet("QMessageBox { font-size: 13px; }")
   ```
5. Connect the `buttonClicked` signal to a slot that prints which button was clicked.
6. Run the message box with `exec_()` and check the result:
   * If the user selects Yes → print `"Cache deleted."`
   * If No → print `"Operation canceled."`
* Pass `self` as the parent when creating the message box.


### Sample Output
> Checkout output.gif For GUI Preview

**UI Behavior:**
* Clicking the button opens a warning dialog with:
  * Title text
  * Extra message below
  * Warning icon
  * Yes and No buttons

**Console Output Example:**
```
User clicked: No
Operation canceled.
```
or
```
User clicked: Yes
Cache deleted.
```
