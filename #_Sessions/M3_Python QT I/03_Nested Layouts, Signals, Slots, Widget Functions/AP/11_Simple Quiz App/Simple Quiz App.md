# 🎯 AP. Simple Quiz App

### Task Objective
In this task, you will:
* Create a quiz interface using PySide2.
* Display a multiple-choice question with four options.
* Provide two buttons: Submit and Reset.
* Display feedback ("Correct!" or "Incorrect!") after submission.
* Disable options after submission and reset on demand.


### Instructions
* Create a `QWidget` window titled **"Quiz Application"**.
* Use `QVBoxLayout` as the main layout.
* Add a `QLabel` to show the question.
* Add four `QRadioButton` widgets to present answer options.
* Group the radio buttons using `QButtonGroup` for exclusive selection.
* Add two `QPushButton` widgets:
  * **Submit**: To evaluate the selected answer.
  * **Reset**: To reset the quiz and enable options again.
* Add a `QLabel` to show feedback after submission.
* When the **Submit** button is clicked:
  * If the selected answer is correct (Paris), show `"Correct!"`.
  * If incorrect, show `"Incorrect!"`.
  * Disable all radio buttons and the Submit button.
* When the **Reset** button is clicked:
  * Clear feedback.
  * Deselect any selected radio button.
  * Enable radio buttons and Submit button again.

### Sample Output
> Check Output.gif