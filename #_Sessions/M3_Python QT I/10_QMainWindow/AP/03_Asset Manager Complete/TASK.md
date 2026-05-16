## 🎯 AP. Asset Manager Complete

### Task Objective:

* Use QMainWindow as the main application window for a VFX-style asset manager tool.
* Implement and organize all five major QMainWindow components:
  * Menu Bar with "File" > "Open" and "Save" actions.
  * Tool Bar with buttons for "Add Asset", "Delete Asset", and "Update Asset".
  * Status Bar to provide feedback when actions are triggered.
  * Dock Widget that displays a list of mock asset entries.
  * Central Widget containing a form layout to input/edit asset information.

### Instructions:

* Create a QMainWindow titled Asset Manager.
* Add a menu bar with a File menu that includes:
  * Open action → triggers "Opening Asset File..." in the status bar.
  * Save action → triggers "Saving Asset File..." in the status bar.
* Add a toolbar with three actions:
  * Add Asset
  * Delete Asset
  * Update Asset
    Each should trigger a corresponding message in the status bar.
* Create a central widget containing a form:
  * Input fields for Asset Name and Asset Type
  * A Submit button that shows a confirmation message in the status bar.
* Add a dock widget on the left side of the main window:
  * The dock widget should display a placeholder list (e.g., asset names like "Tree", "Character", "Vehicle") using any suitable widget (e.g., QListWidget).
* Use the status bar to show feedback for every interaction (menu actions, toolbar clicks, form submission).

### Sample Output:
> Checkout Output.gif for GUI Preview
