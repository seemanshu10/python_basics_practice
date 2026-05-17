## 🎯 **AP. Practice QListView**

### Task Objective

By completing this task, you will:
* Create a list-based UI using `QListView`
* Populate the list using `QStringListModel`
* Set list selection and editing behavior
* Connect the item click signal to update a label
* Apply custom style to the view


### Instructions

You will build a small panel that shows a list of render layers and displays the selected layer.
1. Create a `QWidget` window with a `QVBoxLayout`.
2. Add a `QListView` and a `QLabel` below it.
3. Create a `QStringListModel` with values like:
```python
["Beauty", "Specular", "Diffuse", "ZDepth", "Shadow"]
```
4. Set up the `QListView`:
   * Use `setModel()` to assign the model
   * Use `setEditTriggers(QListView.DoubleClicked)`
   * Use `setSelectionMode(QListView.SingleSelection)`
   * Use `setViewMode(QListView.ListMode)`
5. Connect the `clicked(index)` signal to update the `QLabel` with the selected item’s text.
6. Use `selectedIndexes()` if you want to log the current selected index from within the slot.
7. Style the list using this stylesheet:
```python
view.setStyleSheet("""
QListView {
    background-color: #2b2b2b;
    color: #ffffff;
    font-size: 14px;
    border: 1px solid #555;
}
QListView::item:selected {
    background-color: #007acc;
}
""")
```

### Sample Output
> Checkout Output.gif for GUI Preview

**UI Behavior:**
* Click on `"ZDepth"`
* Label updates: `Selected: ZDepth`
**Console Output:**
```
Item clicked: ZDepth
```
