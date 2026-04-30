## 🎯 AP. Render Queue

### **Task Objective**
In this task, you will:
* Build a PySide2 GUI application to monitor a render queue in a VFX production setting.
* Allow users to add render job names to the queue.
* Display the status of each job as **"In Progress"**.
* Enable users to mark jobs as **"Completed"**.
* Remove in-progress jobs and display completed ones distinctly.

### **Instructions**
**Note: Create Only GUI not Functionality**

* Create a main window titled **"VFX Render Queue"**.
* Add a **QLineEdit** where the user can enter the name of a render job.
* Add a **QPushButton** labeled **"Add Job"**:
  * When clicked, it should add the job to a queue list with a status of **"In Progress"**.
* Add a **QPushButton** labeled **"Mark Completed"**:
  * When clicked, it should remove the selected job from the queue and display it as **"Completed"**.
* Use a **QListWidget** to show all render jobs and their statuses.


### **Sample Output**
> Check Output.gif file for output
