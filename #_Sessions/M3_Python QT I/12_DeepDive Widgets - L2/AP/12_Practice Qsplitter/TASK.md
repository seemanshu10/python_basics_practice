## 🎯 **AP. Practice QSplitter**


### Task Objective

By completing this task, you will:

* Build a horizontal splitter layout using `QSplitter`
* Add two widgets side-by-side: a `QListView` and a `QTextEdit`
* Configure initial sizes and stretch behavior
* Track user interaction with the splitter
* Apply custom style to the splitter handle

### Instructions

You will build a two-panel layout using `QSplitter`.
1. Create a `QWidget` window with a `QVBoxLayout`.
2. Add a `QSplitter` with `Qt.Horizontal` orientation.
3. Inside the splitter, add:
   * A `QListView` on the left
   * A `QTextEdit` on the right
4. Configure the splitter:
   * Use `setSizes([200, 400])` to set initial width of both panels
   * Use `setStretchFactor(0, 1)` to allow the left widget to stretch
   * Use `count()` to get how many widgets are inside (for checking)
   * Use `widget(index)` to print out type of widget at index 0
   * Use `sizes()` to print current size of each widget when moved
5. Connect the `splitterMoved(int, int)` signal to a method that prints:
```
Splitter moved. Position: <pos> Index: <index>
```
6. Style the splitter using:
```python
splitter.setStyleSheet("""
QSplitter::handle {
    background-color: #444;
    width: 6px;
}
""")
```
### Sample Output

> Checkout Output.gif 
* The layout has two resizable panels
* When user drags the handle:
```
Splitter moved. Position: 278 Index: 1
Sizes: [278, 322]
```
