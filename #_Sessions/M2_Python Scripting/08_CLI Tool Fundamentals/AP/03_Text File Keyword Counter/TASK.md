## 🎯 AP. Text File Keyword Counter

### Task Objective

In this task, you will:

* Create a Python script that reads a text file from the command line.
* Accept a keyword as a second command line argument.
* Count how many times the keyword appears in the file, ignoring case.
* Handle cases where the file is missing or the keyword is not found.
* Show a clear message with the result or error.

### Instructions

* Create a script named `keyword_counter.py`.
* The script should accept **two arguments** from the command line: the file path and the keyword to search for.
* Read the content of the file and count how many times the keyword appears (**case-insensitive**).
* If the file doesn’t exist or can’t be opened, print an error message.
* If the keyword is not found, print a message showing that the keyword does not appear.
* If the keyword is found, print how many times it appears.
* Show a usage message if the correct number of arguments is not provided.

---

### 📄 Sample File: `sample.txt`

```
Python is a powerful programming language.
Many developers enjoy using Python because of its simplicity and readability.
With Python, you can build web apps, data pipelines, machine learning models, and more.
This file is used to test how many times the word 'Python' appears.
python is case-insensitive in this search.
Let’s see how accurate the Python keyword counter really is.
```

---

### Sample Output

```
$ python keyword_counter.py sample.txt python
The keyword 'python' appears 5 times.
```

```
$ python keyword_counter.py sample.txt ruby
The keyword 'ruby' was not found in the file.
```

```
$ python keyword_counter.py missing.txt python
Error: The file 'missing.txt' does not exist or cannot be opened.
```

```
$ python keyword_counter.py
Usage: python keyword_counter.py <file_path> <keyword>
```
