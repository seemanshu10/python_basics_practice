## 🎯 AP. Log File Analyzer

### Task Objective

In this task, you will:
* Create a script that takes a log file and one search option as input.
* Filter and display lines that contain `"ERROR"`, `"WARNING"`, or a specific keyword.
* Accept only one search option at a time.
* Handle missing files, missing arguments, or empty results.
* Show clear messages for valid and invalid cases.

### Instructions

* Create a Python script named `log_analyzer.py`.
* Accept a **log file name** as the **first command line argument**.
* Accept **one** of the following as the **second argument**:
  * `--error` to display all lines containing `"ERROR"`
  * `--warning` to display all lines containing `"WARNING"`
  * `--keyword <word>` to search for any specific keyword
* Do **not** allow more than one option at the same time.
* If the file doesn't exist or is empty, show an error.
* If no matching lines are found, display a message.
* Show **usage instructions** when arguments are missing or invalid.
* Use the sample log file below for testing.

---

### Sample Log File: `system.log`

```
INFO: System started successfully.
WARNING: Disk space is running low.
ERROR: Failed to connect to the database.
INFO: User logged in.
ERROR: User authentication failed.
WARNING: High memory usage detected.
INFO: Connection timeout after 30 seconds.
ERROR: Timeout while waiting for server response.
INFO: Scheduled job completed.
```

---

### Sample Output

```
# Error lines
$ python log_analyzer.py system.log --error
ERROR: Failed to connect to the database.
ERROR: User authentication failed.
ERROR: Timeout while waiting for server response.
```

```
# Warning lines
$ python log_analyzer.py system.log --warning
WARNING: Disk space is running low.
WARNING: High memory usage detected.
```

```
# Keyword search
$ python log_analyzer.py system.log --keyword timeout
INFO: Connection timeout after 30 seconds.
ERROR: Timeout while waiting for server response.
```

```
# No matches
$ python log_analyzer.py system.log --keyword reboot
No lines found containing 'reboot'.
```

```
# File doesn't exist
$ python log_analyzer.py missing.log --error
Error: File 'missing.log' does not exist.
```

```
# Missing arguments
$ python log_analyzer.py
Usage: python log_analyzer.py <log_file> [--error | --warning | --keyword <word>]
```
