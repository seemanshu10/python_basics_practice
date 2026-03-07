## 🎯 AP. Color-Coded Log File Viewer

### Task Objective

In this task, you will:

* Use the `colorama` library to apply color formatting to terminal output.
* Read a log file and parse each log entry.
* Map log levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`) to specific colors.
* Display each log entry in color based on its severity level.

### Instructions

* Import and initialize the `colorama` library.
* Define a function that maps log levels to specific colors.
* Read from a file named `log.txt`, line by line.
* For each line:
  * Split the line into timestamp, log level, and message.
  * Apply the appropriate color to the log level and print the line.
  * Use bold text style for all log levels.
  * Reset styles after printing each log entry.

---

### Sample Log File (`log.txt`)

```
2024-08-01 10:00:00 DEBUG: Starting application
2024-08-01 10:01:00 INFO: Configuration file loaded successfully
2024-08-01 10:02:00 WARNING: Memory usage is above threshold
2024-08-01 10:03:00 ERROR: Failed to connect to database
2024-08-01 10:04:00 CRITICAL: System overheating detected
...
```

---

### Sample Output

Each log entry is color-coded:

* **DEBUG** → Blue and bold
* **INFO** → Green and bold
* **WARNING** → Yellow and bold
* **ERROR** → Red and bold
* **CRITICAL** → Magenta and bold

**Check output.png** File