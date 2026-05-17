## 🎯 **AP. Practice QDoubleSpinBox**

### Task Objective

By completing this task, you will:
* Create a UI control for floating-point values using `QDoubleSpinBox`
* Configure its range, step size, decimals, prefix, suffix, and special value text
* Connect signals to track changes and editing completion
* Synchronize the spin box with a slider
* Display the current value in a label
* Apply custom styling to the spin box


### Instructions

You will build a small tool for adjusting **opacity** using floating-point input.
1. Create a `QWidget` window with a `QVBoxLayout`.
2. Add:
   * A `QLabel` for showing the current value
   * A `QDoubleSpinBox`
   * A horizontal `QSlider`
3. Configure the `QDoubleSpinBox` using:
   * `setRange(0.0, 10.0)`
   * `setValue(1.25)`
   * `setSingleStep(0.1)`
   * `setDecimals(2)`
   * `setPrefix("Opacity: ")`
   * `setSuffix(" %")`
   * `setSpecialValueText("Auto")`
4. Connect these signals:
   * `valueChanged(float)` → update the label and update the slider
   * `editingFinished()` → print `"Editing finished"`
5. Configure the `QSlider` to work in range `0–1000`.
6. When the slider changes:
   * Convert its value to float and update the spin box
   * When the spin box changes, update the slider to match
7. Apply this style to the spin box:
```python
spinbox.setStyleSheet("""
QDoubleSpinBox {
    font-size: 14px;
    color: #ffffff;
    background-color: #2e2e2e;
    border: 1px solid #555;
}
""")
```
### Sample Output

> Checkout output.gif

**UI Behavior:**

* Spin box shows: `Opacity: 1.25 %`
* Label displays: `Current Value: 1.25`
* Slider and spin box always move together

**Console Output**
```
New value: 2.10
Editing finished
```
