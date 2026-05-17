## 🎯 **AP. Practice QScrollArea**

### Task Objective

By completing this task, you will:
* Create a scrollable area using `QScrollArea`
* Place a long list of widgets (e.g. labels) inside the scroll area
* Configure scrolling behavior using scrollbar policies
* Use a button to scroll to a specific part of the content
* Track scrolling with `valueChanged` signal
* Apply basic visual styling to the scroll area and scrollbars


### Instructions

You will build a window that contains a scrollable list of items.
1. Create a `QWidget` window with a `QVBoxLayout`.
2. Inside the main layout, add:
   * A `QPushButton` labeled **"Scroll to Bottom"**
   * A `QScrollArea` widget
3. Inside the scroll area:
   * Add a content widget (use a `QWidget`)
   * Set a `QVBoxLayout` on this widget
   * Add at least **30 `QLabel`s** to simulate a long list
   * Set this content widget into the scroll area using `setWidget()`
   * Call `setWidgetResizable(True)`
4. Configure scroll behavior using:
   * `setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)`
   * `setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)`
5. Connect:
   * The button’s `clicked()` signal to scroll to the bottom using `ensureVisible(x, y)`
   * The scroll area's **vertical scrollbar’s** `valueChanged(int)` signal to print the current scroll value
6. Style the scroll area using this stylesheet:
```python
scroll_area.setStyleSheet("""
QScrollArea {
    background-color: #2c2c2c;
}
QScrollBar:vertical {
    background: #444;
    width: 10px;
}
""")
```

### Sample Output
> Checkout output.gif for GUI Preview

* Scrollable vertical list of labels: `Item 1` to `Item 30+`
* Button at top scrolls to the bottom when clicked
**Console Output Example (when scrolling):**
```
Scroll position: 72
Scroll position: 165
```
