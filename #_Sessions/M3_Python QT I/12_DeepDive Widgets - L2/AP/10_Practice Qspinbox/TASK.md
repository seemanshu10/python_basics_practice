## 🎯 **AP. Practice QSpinBox**

### Task Objective

By completing this task, you will:
* Create a basic UI using `QSpinBox` to control numeric input
* Set the range, default value, step size, prefix, suffix, and special value text
* Use signals to detect changes and editing completion
* Display the current value in a `QLabel`
* Apply styling to the spinbox

### Instructions

You will build a widget where users can select a frame number using a `QSpinBox`.
1. Create a `QWidget` window with a `QVBoxLayout`.
2. Add:
   * A `QSpinBox`
   * A `QLabel` to show the selected value
3. Set up the `QSpinBox` using:
   * `setRange(0, 200)`
   * `setValue(10)`
   * `setSingleStep(5)`
   * `setPrefix("Frame ")`
   * `setSuffix(" px")`
   * `setSpecialValueText("Auto")`
4. Connect:
   * `valueChanged(int)` → update the label to show the new value
   * `editingFinished()` → print `"User finished editing"` to the console
5. Apply this style to the spinbox:
```python
spinbox.setStyleSheet("""
QSpinBox {
    font-size: 14px;
    color: #ffffff;
    background-color: #2b2b2b;
    border: 1px solid #666;
}
""")
```

### Sample Output
> Checkout output.gif for output Preview

**UI Behavior:**
* The spinbox shows values like `Frame 10 px`
* When value is 0, it shows `Auto` instead
* Label below displays: `Selected: 10`
**Console Output Example:**
```
User finished editing
```