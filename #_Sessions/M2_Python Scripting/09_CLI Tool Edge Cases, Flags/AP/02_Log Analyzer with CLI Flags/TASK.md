## AP. Log Analyzer with CLI Flags

### Task Objective

In this task, you will:

* Build a command-line tool to analyze log files used in VFX pipelines.
* Filter log entries by severity level (`INFO`, `WARNING`, `ERROR`, `CRITICAL`) using flags.
* Add a `--verbose` flag to print debug information during execution.
* Add a `--reverse` flag to reverse the output order of filtered logs.
* Handle missing files and unknown flags gracefully.

### Instructions

* Write a Python script named `log_analyzer.py`.
* The script must accept a **log file path** as a required **positional argument**.
* The script should support the following **optional flags**:
  * `--info` – show only INFO messages.
  * `--warning` – show only WARNING messages.
  * `--error` – show only ERROR messages.
  * `--critical` – show only CRITICAL messages.
  * `--reverse` – reverse the order of the displayed logs.
  * `--verbose` – show debug info like which file is being opened and what filter is used.
* If **no filter flags** are provided, all log messages should be displayed.
* If an **invalid flag** is passed or if the **file doesn't exist**, display an error message.

---

### Sample Log File: `logs.txt`

```
2024-07-23 09:05:00 INFO: Application started successfully.
2024-07-23 09:10:00 WARNING: Low memory warning. Available memory is below the threshold.
2024-07-23 09:15:00 ERROR: FileNotFound: Unable to locate the configuration file.
2024-07-23 09:20:00 CRITICAL: SystemCrash: The application has encountered a critical error and needs to close.
2024-07-23 09:25:00 INFO: Memory cleanup process initiated.
2024-07-23 09:35:00 ERROR: NullReference: Attempted to access an object that is null.
```

---

### Expected Outputs

**Example 1: Displaying ERROR Logs**

**Command:**

```
python log_analyzer.py logs.txt --error
```

**Output:**

```
2024-07-23 09:15:00 ERROR: FileNotFound: Unable to locate the configuration file.
2024-07-23 09:35:00 ERROR: NullReference: Attempted to access an object that is null.
```

---

**Example 2: Displaying INFO Logs in Reverse Order**

**Command:**

```
python log_analyzer.py logs.txt --info --reverse
```

**Output:**

```
2024-07-23 09:25:00 INFO: Memory cleanup process initiated.
2024-07-23 09:05:00 INFO: Application started successfully.
```

---

**Example 3: Running with --verbose**

**Command:**

```
python log_analyzer.py logs.txt --error --verbose
```

**Output:**

```
[DEBUG] Opening file: logs.txt
[DEBUG] Filtering messages with keyword: ERROR
2024-07-23 09:15:00 ERROR: FileNotFound: Unable to locate the configuration file.
2024-07-23 09:35:00 ERROR: NullReference: Attempted to access an object that is null.
```

---

**Example 4: Handling an Invalid Flag**

**Command:**

```
python log_analyzer.py logs.txt --invalidflag
```

**Output:**

```
Error: Unknown flag '--invalidflag'. Use '--help' for instructions.
```
