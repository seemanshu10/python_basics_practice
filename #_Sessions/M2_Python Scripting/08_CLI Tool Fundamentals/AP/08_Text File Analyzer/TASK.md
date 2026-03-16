## 🎯 AP. Text File Analyzer

### Task Objective

In this task, you will:
* Write a Python script that takes a text file path as input from the command line.
* Analyze the file to count words, lines, characters, or find the longest word.
* Support multiple analysis options passed together.
* Show a help message if no analysis option is given.
* Handle missing files or missing file paths with clear error messages.

### Instructions

* Create a Python script named `text_analyzer.py`.
* Accept the text file using `-f` or `--file` followed by the file path.
* Support the following optional analysis flags:
    * `-w` or `--words`: Count total words
    * `-l` or `--lines`: Count total lines
    * `-c` or `--characters`: Count total characters
    * `-lw` or `--longest-word`: Show the longest word in the file
* The user can combine multiple flags in one command.
* If no analysis option is passed, display usage instructions.
* If the file is missing or not provided, show an error message.
* Use the sample file below to test the script.

### Sample Text File: `sample.txt`

```
Python is a powerful programming language.
It is widely used in data science, web development, and automation.
This text file is used for testing the text analyzer script.
Let's see how many lines, words, characters, and what the longest word is.
```

### Sample Output

```
# Count words
$ python text_analyzer.py -f sample.txt -w
Number of words:  thirty-one (31)

# Count lines
$ python text_analyzer.py -f sample.txt -l
Number of lines: 4

# Count characters
$ python text_analyzer.py -f sample.txt -c
Number of characters: 229

# Show longest word
$ python text_analyzer.py -f sample.txt -lw
Longest word: development

# Multiple options
$ python text_analyzer.py -f sample.txt -w -l -c
Number of words: 31
Number of lines: 4
Number of characters: 229

# No file path
$ python text_analyzer.py -w
Error: No file path provided. Use -f or --file to specify the file path.

# No analysis option
$ python text_analyzer.py -f sample.txt
Please specify at least one analysis option: -w, -l, -c, or -lw.

# File doesn't exist
$ python text_analyzer.py -f notfound.txt -w
Error: The file 'notfound.txt' does not exist.
```
