## 🎯 AP. Render Shot Status & Tool Launch

### Task Objectives

In this task, you will:

* Use sys.argv to accept one or more shot IDs from the command line
* Read shot metadata from a pre-supplied render_status.json file
* Display information like status, artist, frame range, and notes for each shot
* Use Colorama to visually highlight different status types

### Instructions
* You are provided with a file named render_status.json that contains metadata for ~50 shots, including status, artist, frame range, last update, and notes.
* Create a Python script named check_render.py inside a folder named render_tool.
* Your script must:
  * Accept one or more shot IDs passed as command-line arguments via sys.argv
  * Load and parse render_status.json from the same folder
* For each shot ID:
  * If the shot exists in the JSON file:
  * Print its metadata (status, artist, frame range, last update, notes)
  * Use Colorama to color-code the output:
  * Green if status is rendered
  * Yellow if status is rendering
  * Red if status is failed
  * Reset color after each shot using autoreset=True
* If the shot is not found:
  * Print a plain message: ⚠️ Shot not found. (no color needed)
* Create a batch file named render_check.bat in the same folder.
* The batch file must
  * Use %~dp0 to call check_render.py
  * Accept any number of shot IDs as arguments (1 or more)
  * Pass them all to the Python script using %*
  * Include pause at the end to keep the window open
  * render_status.json given alogn with this task do check

### Sample Output
* Do check output.png for sample output.