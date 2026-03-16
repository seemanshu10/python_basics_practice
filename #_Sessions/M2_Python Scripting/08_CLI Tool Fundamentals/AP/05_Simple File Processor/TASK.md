## 🎯 AP. Simple File Processor

### Task Objective

In this task, you will:

* Create a script that reads a file and performs a specific action selected by the user.
* Support three possible actions: count lines, count words, or count characters.
* Accept the action and the file name as command line arguments.
* Validate that only one action is given at a time.
* Handle errors for missing files, missing arguments, or invalid actions.

### Instructions

* Create a Python script named `file_processor.py`.
* Make the script accept **two command line arguments**: one **action** and one **file name**.
* The action must be one of the following:
  * `--lines` to count lines
  * `--words` to count words
  * `--chars` to count characters
* If **more than one action** is provided, show an error message.
* If the file does **not exist**, show an error message.
* If **no arguments** are provided, show usage instructions.
* Run the script with different actions to test the results.

---

### Sample Output

```
# Count lines
$ python file_processor.py --lines sample.txt
Number of lines: 10
```

```
# Count words
$ python file_processor.py --words sample.txt
Number of words: 50
```

```
# Count characters
$ python file_processor.py --chars sample.txt
Number of characters: 250
```

```
# Multiple actions
$ python file_processor.py --lines --words sample.txt
Error: Please specify only one action (--lines, --words, --chars)
```

```
# Missing file
$ python file_processor.py --lines nonexistent.txt
Error: File 'nonexistent.txt' not found.

```

```
# No arguments
$ python file_processor.py
Usage: python file_processor.py <action> <filename>
Actions:
  --lines  : Count lines in the file
  --words  : Count words in the file
  --chars  : Count characters in the file

```
