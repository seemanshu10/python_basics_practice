## 🎯 AP. Utility Panel 

### **Task Objective**

In this task, you will:
* Create a main window using `QMainWindow` as the application container.
* Add a basic menu bar, toolbar, and status bar to the main window.
* Use a `QSplitter` to divide the central area of the application horizontally into two resizable sections.
* On the **left side**, add a `QDockWidget` that contains:
  * A `QTreeView` to represent a nested asset structure.
  * A `QListView` to display a list of asset categories.
  * A `QTableView` to show metadata such as name, version, and status.
* On the **right side**, add a `QScrollArea` that contains:
  * A `QSpinBox` for frame input.
  * A `QDoubleSpinBox` for opacity or scale adjustment.
  * A button to open a `QFileDialog` and select an image file.
  * A `QLabel` to display the selected image using `QPixmap`.
  * A button to open a `QColorDialog` and apply a selected color as a border.
  * A button to open a `QFontDialog` and apply the selected font to the label text.



### **Instructions**

* Set up a `QMainWindow` with:
  * A menu bar containing a "File" menu and Exit action.
  * A toolbar that includes the same Exit action.
  * A status bar that shows a default message (e.g., "Ready").
* Use a `QSplitter` as the central widget of the main window to split the layout into two parts.
* On the left side of the splitter:
  * Create a `QDockWidget`.
  * Inside the dock, add a vertical layout that includes:
    * A `QTreeView` with a few parent-child items.
    * A `QListView` with a static string list model.
    * A `QTableView` with 3 columns and some mock data.
* On the right side of the splitter:
  * Create a `QScrollArea`.
  * Inside the scroll area, add a widget with a `QGridLayout` or `QFormLayout`.
  * Add these components to the layout:
    * A `QSpinBox` with a suitable range.
    * A `QDoubleSpinBox` with a step size (e.g., 0.05).
    * A button to open a file dialog and load an image.
    * A `QLabel` to preview the image using `QPixmap`.
    * A button to open a color dialog and apply border color to the image.
    * A button to open a font dialog and apply the font to the label.
* Ensure all buttons are connected to their respective dialogs.


### **Sample Output**

**UI structure preview:**
> Check Output.png for GUI Preview

**Console output sample:**

```
Loaded file: /Users/assets/char01.jpg
Selected color: #ccff00
Selected font: Helvetica,10,-1,5,50,0,0,0,0,0
```
