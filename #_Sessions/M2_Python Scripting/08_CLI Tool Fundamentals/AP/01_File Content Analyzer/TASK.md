## 🎯 AP. File Content Analyzer

### Task Objective

In this task, you will:
* Create a Python script that takes a file path from the command line.
* Count how many words are in the file (case-insensitive, punctuation removed).
* Count how many characters are in the file, including spaces.
* Count how many lines are in the file.
* Show an error if the file path is missing or the file doesn’t exist.

### Instructions

* Create a script named `file_analyzer.py`.
* Make the script read a file from the command line.
* If the file doesn’t exist, print an error and stop.
* If no file is given, show a message asking for one.
* Read the file and count:
  * **Words** (ignore punctuation and case)
  * **Characters** (include spaces)
  * **Lines**
* Print all three values clearly in the terminal.

---

### Sample File: `sample.txt`

```
Hello, this is a simple text file.
It contains multiple lines,
some punctuation, and words repeated — like simple, SIMPLE, and Simple.
Total words should be counted case-insensitively.
There are empty lines too.

This is the last line.
```

---

### Sample Output

```
$ python file_analyzer.py sample.txt
Total Words: 100
Total Characters: 450
Total Lines: 20
```

```
$ python file_analyzer.py
Error: No file path provided. Please provide the path to a text file.
```

```
$ python file_analyzer.py nonexistent.txt
Error: The file 'nonexistent.txt' does not exist.
```
