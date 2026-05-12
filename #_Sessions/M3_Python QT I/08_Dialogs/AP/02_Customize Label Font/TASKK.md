## 🎯 AP. Customize Label Font 

### **Task Objective**

**In this task, you will:**

* Build a PySide2 interface that lets users pick a font for review labels.
* Use `QFontDialog.getFont()` to open the system font selection dialog.
* Apply the selected font to a `QLabel`.
* Display the chosen font’s family, size, and style (bold/italic) in the label.
* Simulate a common VFX tool use case where artists configure overlay text styles for review or slates.


### **Instructions**

* Create a QWidget-based UI using PySide2.
* Add a button labeled **"Choose Font"**.
* When the button is clicked:
  * Open the font selection dialog.
  * If the user confirms a selection:
    * Apply the selected font to a label.
    * Update the label’s text to show:
      * Font family (e.g. Arial)
      * Font size in points (e.g. 14pt)
      * Whether the font is bold or normal
      * Whether the font is italic or regular
* If the user cancels the font dialog, leave the label unchanged.

### **Sample Output**

> For GUI Preview CHeckout :- Output.gif

If the user picks a font:
```
Nirmala UI, 18pt, Bold, Italic
```

The label will display this text using the selected font.
If canceled:
```
Review label here
```
