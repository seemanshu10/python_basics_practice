## AP. Log Summary Generator

### Task Objective

Create a Python CLI tool that:

* Reads a VFX log file.
* Counts log level occurrences: `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.
* Tracks the most recent entry for each log level.
* Prints a clean summary report.
* Handles missing arguments, nonexistent files, and empty files.

---

### Instructions

Create a script named `log_summary.py`.

The script must:

* Accept the **log file path** as a **command-line argument**.
* Count occurrences of each log level.
* Track the **latest entry per log level**.
* Print a summary report in this format:

```
INFO:     2 occurrences | Last Entry: [...]
```

Show proper error messages if:

* **No argument is passed**
* The **file does not exist**
* The **file is empty**
* The file **can’t be read**

---

### Sample Log File – `logs.txt`

```
[2024-02-01 10:05:12] INFO: Render started for shot_001
[2024-02-01 10:06:15] WARNING: Memory usage is high
[2024-02-01 10:07:30] ERROR: Failed to load texture asset_03.png
[2024-02-01 10:08:45] INFO: Render completed for shot_001
[2024-02-01 10:09:50] CRITICAL: Renderer crashed unexpectedly
[2024-02-01 10:10:05] ERROR: File missing in directory assets/
[2024-02-01 10:11:20] WARNING: Disk space running low
```

---

### Example Command

```
python log_summary.py logs.txt
```

---

### Expected Output

```
Log Summary Report
------------------
INFO:     2 occurrences | Last Entry: [2024-02-01 10:08:45] INFO: Render completed for shot_001
WARNING:  2 occurrences | Last Entry: [2024-02-01 10:11:20] WARNING: Disk space running low
ERROR:    2 occurrences | Last Entry: [2024-02-01 10:10:05] ERROR: File missing in directory assets/
CRITICAL: 1 occurrence  | Last Entry: [2024-02-01 10:09:50] CRITICAL: Renderer crashed unexpectedly
```
