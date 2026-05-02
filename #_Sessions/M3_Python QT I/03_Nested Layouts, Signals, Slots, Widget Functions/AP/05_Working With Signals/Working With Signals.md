## 🎯 AP. Working with Signals

### **Task Objective**

In this task, you will:
* Build a PySide2 application that demonstrates how **signals** work with common UI widgets.
* Connect at least one signal from each widget to a function.
* Observe and print feedback in the console whenever the user interacts with the UI.

### **Instructions**
* Create a main window using `QWidget`.
* Use either `QVBoxLayout` or `QHBoxLayout` to organize the interface.
* Add the following widgets to the layout:
  * `QPushButton`
  * `QRadioButton`
  * `QLabel`
  * `QLineEdit`
  * `QSlider`
  * `QCheckBox`
  * `QComboBox`
  * `QGroupBox`
  * `QTextEdit`
* For each widget, connect **at least one signal** to a function that prints a message to the console.
* Display the window and verify that interacting with the widgets produces console output.


### **Sample Output**
> Refere Output.gif gor output

```
Button clicked!
Radio Button selected: Option 1
Text entered: Hello World
Slider value changed: 40
Checkbox checked
ComboBox selected: Item 2
GroupBox toggled: True
Text changed in QTextEdit. Word count: 5
```
