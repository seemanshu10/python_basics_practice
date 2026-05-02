## 🎯 AP. User Form UI

### **Task Objective**

In this task, you will:
* Build a complete PySide2 user form using nested vertical and horizontal layouts.
* Collect personal details, preferences, and feedback from the user.
* Use a variety of widgets in one cohesive interface.
* Display a formatted summary of the user’s input inside the application.


### **Instructions**
👉 **Refer to the `output.png` image for layout and widget placement before starting this task. Your UI should closely match the structure shown in that image.**
* Create the main window using `QWidget` and set the title to **"Advanced User Form"**.
* Use nested `QVBoxLayout` and `QHBoxLayout` to organize all sections of the form.
* Add the following interface elements:
  * A **title label** at the top: `"User Feedback Form"`.
  * Two **QLineEdit** fields for entering **First Name** and **Last Name**.
  * Three **QRadioButton** widgets for selecting **Gender**: Male, Female, Other.
  * Three **QCheckBox** widgets for selecting **Interests**: Music, Sports, Reading.
  * A **QTextEdit** for writing **Comments/Feedback**.
  * A **QSlider** (range 1–10) for **Rating**, with a **QLabel** showing the current value.
  * A **QComboBox** to select **Preferred Contact Method**: Phone, Email, SMS.
  * A **QPushButton** labeled **Submit**.
  * A **QTextBrowser** that shows the summary of all input after form submission.
* When the Submit button is pressed, gather all the inputs and display a formatted summary in the QTextBrowser.


### **Sample Output**

```
First Name: Alex
Last Name: Carter
Gender: Male
Interests: Music, Reading
Feedback: Great interface!
Rating: 8
Preferred Contact: Email
```