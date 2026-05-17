## 🎯 **AP. Practice QTableView**

### Task Objective

By completing this task, you will:
* Build a table using `QTableView` and populate it using `QStandardItemModel`
* Control editing, selection, and sorting behavior
* Connect a signal to print selected row and column
* Apply column width control and auto-fit behavior
* Style the table and headers using CSS


### Instructions

You will create a table showing render job data with two columns: **"Shot"** and **"Status"**.
1. Create a `QWidget` window with a `QVBoxLayout`.
2. Add a `QTableView` to the layout.
3. Use `QStandardItemModel` to create a table with 3 rows and 2 columns.
4. Fill the model with data like:
```python
[["Shot001", "Queued"], ["Shot002", "Rendering"], ["Shot003", "Completed"]]
```
5. Set up the table with the following:
   * Use `setModel()` to assign the model
   * Use `setEditTriggers(QTableView.DoubleClicked)` to allow editing
   * Use `setSelectionBehavior(QTableView.SelectRows)` to select by row
   * Use `setSelectionMode(QTableView.SingleSelection)` to allow single selection
   * Use `setSortingEnabled(True)` to enable sorting
   * Use `selectRow(1)` to auto-select the second row
   * Use `setColumnWidth(0, 150)` to fix the width of the first column
   * Use `resizeColumnsToContents()` to fit column sizes
6. Connect the `clicked(index)` signal to a method that prints:
```
Clicked cell at row: <row> column: <column>
```
7. Apply the following stylesheet to your table:
```python
table.setStyleSheet("""
QTableView {
    background-color: #2e2e2e;
    color: #f1f1f1;
    gridline-color: #444;
    font-size: 13px;
}
QHeaderView::section {
    background-color: #3c3c3c;
    padding: 4px;
    font-weight: bold;
    border: 1px solid #222;
}
QTableView::item:selected {
    background-color: #007acc;
}
""")
```


### Sample Output
> Checkout output.gif

When a user clicks a cell, the console shows:
```
Clicked cell at row: 2 column: 1
```
Row 2 appears preselected.

