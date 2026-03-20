## AP: Shot Log Processor

### Task Objective

In this task, you will:

* Create a command-line tool that reads and filters a VFX shot log file.
* Filter log lines based on a keyword provided by the user (e.g., `RENDERED`, `FAILED`).
* Handle different types of user errors such as missing files, invalid keywords, or incorrect arguments.
* Prevent the script from crashing by using proper error handling.

### Instructions

Create a Python script named `shot_log_processor.py`.

Accept exactly **two command-line arguments**:

* **First**: the path to a `.log` file.
* **Second**: a filter keyword (`RENDERED` or `FAILED`).

Handle the following:

* If too many or too few arguments are passed, show an error message.
* If the file does not exist, show an error message.
* If the filter keyword is invalid, show an error message.
* Read the file and print only the lines that match the filter keyword.
* If an unexpected error occurs (e.g., a coding bug), catch it and print a fallback error message.

Use the sample file below to test your script.

---

### Sample Log File: `shots.log`

```
SHOT_001 RENDERED
SHOT_002 FAILED
SHOT_003 RENDERED
SHOT_004 FAILED
SHOT_005 RENDERED
```

---

### Expected Output

**Test Case 1: Valid Inputs**

**Command:**

```
python shot_log_processor.py shots.log RENDERED
```

**Output:**

```
SHOT_001 RENDERED
SHOT_003 RENDERED
SHOT_005 RENDERED
```

---

**Test Case 2: Non-Existent File**

**Command:**

```
python shot_log_processor.py missing_shots.log RENDERED
```

**Output:**

```
ERROR: The file 'missing_shots.log' does not exist. Please provide a valid file path.
```

---

**Test Case 3: Invalid Filter Argument**

**Command:**

```
python shot_log_processor.py shots.log COMPLETED
```

**Output:**

```
ERROR: Invalid filter: COMPLETED. Accepted values are 'RENDERED' or 'FAILED'.
```

---

**Test Case 4: Too Many Arguments**

**Command:**

```
python shot_log_processor.py shots.log RENDERED EXTRA_ARG
```

**Output:**

```
ERROR: Too many arguments. Only two arguments are allowed.
```

---

**Test Case 5: Too Few Arguments**

**Command:**

```
python shot_log_processor.py shots.log
```

**Output:**

```
ERROR: At least two arguments are required: a file path and a filter keyword.
```

---

**Test Case 6: Unexpected Error (Simulated)**

*Modify the script to introduce an unexpected error:*

```python
raise RuntimeError("Simulating an unexpected error")
```

**Command:**

```
python shot_log_processor.py shots.log RENDERED
```

**Output:**

```
An unexpected error occurred: Simulating an unexpected error
```
