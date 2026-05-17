## 🎯 **AP. Practice QDockWidget**

### Task Objective

By completing this task, you will:
* Create a main window with a dockable side panel
* Use `QDockWidget` and connect it to `QMainWindow`
* Add a simple widget (like a `QLabel`) inside the dock
* Use all common methods to configure the dock
* Connect signals to track docking behavior
* Apply basic styling to the dock widget and its title bar


### Instructions

You will build a main window with a right-side dock panel.
1. Create a class that inherits from `QMainWindow`.
2. Set the window title and size using `setWindowTitle()` and `resize()`.
3. Create a central widget (e.g., `QLabel("Main Content")`) and set it using `setCentralWidget()`.
4. Create a `QDockWidget`:
   * Use `setWindowTitle("Inspector Panel")`
   * Add a child widget inside it using `setWidget()` (e.g., a `QLabel("Properties go here")`)
   * Use `setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)`
   * Use `setFloating(False)`
   * Use `setVisible(True)`
   * Use `setFeatures(QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetMovable)`
   * Use `toggleViewAction()` and add the action to the View menu
5. Add the dock widget to the **right** side of the main window using `addDockWidget()`.
6. Connect these signals from the dock widget:
   * `visibilityChanged(bool)` → print `"Dock visible:"` and the value
   * `topLevelChanged(bool)` → print `"Floating:"` and the value
   * `dockLocationChanged(Qt.DockWidgetArea)` → print `"Moved to area:"` and the area value
7. Apply this stylesheet to the dock:
```python
dock.setStyleSheet("""
QDockWidget {
    background-color: #2b2b2b;
    color: #ffffff;
}
QDockWidget::title {
    background-color: #444444;
    padding: 6px;
}
""")
```

### Sample Output

> Checkout output.gif 

* Central label says: **"Main Content"**
* Dock on the right shows: **"Inspector Panel"** with **"Properties go here"**
* View menu contains toggle for showing/hiding the dock
* Console logs when dock is hidden, moved, or floated

**Example console output:**
```
Dock visible: True
Floating: False
Moved to area: 2
```
