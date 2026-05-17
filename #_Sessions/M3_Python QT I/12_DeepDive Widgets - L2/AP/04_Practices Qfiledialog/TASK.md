## 🎯 **AP. Creating a Custom File Picker with QFileDialog**

### Task Objective

By completing this task, you will:
* Use `QFileDialog` to create a custom file picker window
* Configure all its basic methods
* Connect important signals
* Integrate with other UI widgets (`QPushButton`, `QLineEdit`, `QLabel`)
* Apply basic dialog styling using `setStyleSheet`

### Instructions

You need to build a simple file picker interface using PySide2.
1. Create a `QWidget` window with vertical layout using `QVBoxLayout`.
2. Add these widgets to the layout in this order:
   * `QLineEdit` → to display the selected file path
   * `QPushButton` → label it **“Browse”**
   * `QLabel` → default text should be **“Status: Waiting for input...”**
3. When the button is clicked, open a custom `QFileDialog` instance (do not use static methods).
   Use the following methods to configure the dialog:
   * `setFileMode(QFileDialog.ExistingFile)`
   * `setNameFilter("Images (*.exr *.png *.jpg)")`
   * `setDirectory("./assets")`
   * `selectFile("sample.exr")`
   * `setViewMode(QFileDialog.Detail)`
   * `setOption(QFileDialog.ShowDirsOnly, False)`
4. Connect the following signals:
   * `fileSelected(str)` → update the `QLineEdit` and `QLabel` with the file path
   * `currentChanged(str)` → print the currently selected file to the console
   * `directoryEntered(str)` → print the current folder to the console
   * `filterSelected(str)` → print the selected filter to the console
5. Apply this stylesheet to the dialog:
```python
dialog.setStyleSheet("QFileDialog { font-size: 14px; }")
```
6. Run the dialog using `exec_()` to make it modal.
7. Make sure to pass `self` as the parent when creating the dialog.


### Sample Output

> Checkout output.gif for Preview

**Console prints when interacting with the dialog:**
```
Current file: ./assets/sample.exr
Entered dir: ./assets/textures
Filter: Images (*.exr *.png *.jpg)
File selected: ./assets/sample.exr
```
