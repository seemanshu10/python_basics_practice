## 🎯 AP. Launch a DCC Application Using a Bat File

### ✅ Task Objective

In this task, you will:

* Write a batch script to launch a DCC application from a Windows system.
* Prioritize launching in this order: **Nuke → Maya → Houdini**.
* If none of the above are installed, the script should launch **Notepad** as a fallback.
* Practice basic automation using the `start` command in `.bat` scripts.

---

### Instructions

Create a batch file named `launch_dcc.bat`.

In this script, you will:
* Use the `start` command to attempt launching:
  * Nuke
  * Maya
  * Houdini
  * Fallback: Notepad
* All applications will be listed in **priority order**.
* The script will try each application one after another in the order written.
  If an application isn’t installed, it will **silently skip** to the next.

---

### Sample Output Behavior

Run this command in your terminal:

```
launch_dcc.bat
```

Depending on which application is available:

* If **Nuke** is installed → Nuke will launch.
* If **Nuke** is missing but **Maya** is installed → Maya will launch.
* If only **Houdini** is available → Houdini will launch.
* If **none** are found → **Notepad** will launch.
