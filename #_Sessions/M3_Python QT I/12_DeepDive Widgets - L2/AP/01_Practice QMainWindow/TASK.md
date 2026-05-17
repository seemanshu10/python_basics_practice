## 🎯 AP. Practicing QMainWindow

### **Task Objective**

By the end of this task, you will:

* Create a `QMainWindow`-based GUI using PySide2
* Add a central `QTextEdit` widget for text input
* Set up a menu bar with `File` and `View` menus
* Add `Clear` and `Exit` actions to both the menu and toolbar
* Add a dockable panel labeled “Inspector” on the right
* Display real-time messages using a `QStatusBar`
* Apply a basic dark-themed stylesheet for a studio-style look


### **Instructions**

Follow these steps to complete your task:

* Build a main window using `QMainWindow`
* Set the window title and size
* Add a central widget using `QTextEdit`
* Create a menu bar with
  * A **File** menu containing `Clear` and `Exit` actions
  * A placeholder **View** menu (no functionality needed yet)
* Connect the `Clear` action to clear the text editor
* Add a toolbar with the same `Clear` and `Exit` actions
* Add a `QDockWidget` on the right side labeled **Inspector** with a basic label inside
* Use `QStatusBar` to display status messages (e.g., “Ready”, “Editor cleared”)
* Apply a simple stylesheet to make the UI look professional


### Sample Output
> Checkout the Output.gif for GUI Preview