## 🎯 AP. Asset Submission Form

### **Task Objective**

In this task, you will:
* Build a PySide2 GUI application to simulate a VFX asset submission form.
* Allow users to input an asset name and select an asset type from a dropdown list.
* Add form validation to ensure that all required fields are filled before submission.
* Display success or error messages based on the input validation.


### **Instructions**
**Note: Create Only GUI not Functionality**

* Create a main window titled **"VFX Asset Submission"**.
* Add a **QLineEdit** where the user can enter the asset name.
* Add a **QComboBox** with a default item like **"Select Asset Type"**, and additional items: **"Texture"**, **"Model"**, **"Render"**.
* Add a **QPushButton** labeled **"Submit"** to trigger the form submission.
* Add a **QLabel** to display the result message (either success or error).
* When the submit button is clicked:
  * Check that the asset name is not empty.
  * Ensure the user has selected a valid asset type (not the default).
  * If validation fails, show an error message in the label.
  * If validation passes, show a simulated success message in the label.


### **Sample Output**
> Check Output.gif file for output
