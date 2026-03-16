## 🎯 AP. Directory Size Calculator

### Task Objective

In this task, you will:
* Write a Python script that takes a directory path from the command line.
* Calculate the total size of all files inside that directory and its subdirectories.
* Show the result in **bytes**, **kilobytes**, or **megabytes** based on a single flag.
* Validate the directory path and handle invalid or missing input.
* Handle multiple flags by showing an error message.

### Instructions

* Create a Python script named `dir_size_calculator.py`.
* Accept a directory path as the **first command line argument**.
* Accept **one optional flag**: `--bytes`, `--kilobytes`, or `--megabytes`.
* Only allow **one** of the size flags. If multiple are passed, show an error and exit.
* If **no flag** is passed, default to showing size in **bytes**.
* If the directory does **not exist**, print an error message.
* Recursively calculate the size of all files inside the directory.
* Print the total size in the selected format.

---

### Sample Output

```
# Size in bytes
$ python dir_size_calculator.py /path/to/directory --bytes
Total size: 1048576 bytes
```

```
# Size in kilobytes
$ python dir_size_calculator.py /path/to/directory --kilobytes
Total size: 1024.00 KB
```

```
# Size in megabytes
$ python dir_size_calculator.py /path/to/directory --megabytes
Total size: 1.00 MB
```

```
# Multiple options
$ python dir_size_calculator.py /path/to/directory --bytes --kilobytes
Error: Please specify only one option (--bytes, --kilobytes, --megabytes).
```

```
# Directory doesn't exist
$ python dir_size_calculator.py /nonexistent/directory --bytes
Error: Directory '/nonexistent/directory' does not exist.
```
