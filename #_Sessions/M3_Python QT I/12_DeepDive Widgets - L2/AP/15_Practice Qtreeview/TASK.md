## 🎯 AP. Practice QTreeView

### Task Objective

By completing this task, you will:
* Create a `QTreeView` to display hierarchical data using `QStandardItemModel`.
* Use editing, selection behavior, and column resizing methods.
* Expand and collapse nodes with signals and buttons.
* Connect basic signals like `clicked` and `expanded`.
* Apply styling to rows and headers.


### Instructions
You will build a panel to display a nested VFX asset structure using `QTreeView`.
The tree should contain a hierarchy like this:
```
Character
 └── Rig
     └── Controls
Environment
 └── Terrain
 └── Lighting
```
1. Set up a main `QWidget` window with a `QVBoxLayout`.
2. Add a `QTreeView` to the layout.
3. Use `QStandardItemModel` to create and assign a tree model to the view using `setModel()`.
4. Set the following on the `QTreeView`:
   * `setEditTriggers(QTreeView.DoubleClicked)`
   * `setSelectionMode(QTreeView.SingleSelection)`
   * `setSelectionBehavior(QTreeView.SelectRows)`
   * `setColumnWidth(0, 200)`
   * `resizeColumnToContents(0)`
5. Expand all nodes on startup using `expandAll()`.
6. Connect these signals:
   * `clicked(index)` → print the item name
   * `expanded(index)` → print "Expanded: <item name>"
7. Add two `QPushButton`s below the tree:
   * One for collapsing all nodes (connect to `collapseAll()`)
   * One for expanding all nodes (connect to `expandAll()`)
8. Apply the following stylesheet:
```python
tree.setStyleSheet("""
QTreeView {
    background-color: #2b2b2b;
    color: #ffffff;
    font-size: 13px;
    border: 1px solid #444;
}
QTreeView::item:selected {
    background-color: #007acc;
}
QHeaderView::section {
    background-color: #3c3c3c;
    font-weight: bold;
}
""")
```

### Sample Output

>Checkout output.gif for GUI Preview

* Tree shows nested data in collapsible form.
* Clicking a node prints its name.
* Buttons let the user expand or collapse all nodes.

```
Clicked item: Controls
Expanded: Rig
```