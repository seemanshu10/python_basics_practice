## 🎯 AP. Data Processor Module

### Task Objective

* Create a Python module named `log_processor.py` to process text-based log files.
* Implement three functions in the module: count lines, count words, and count characters.
* Create a second script, `analyze_logs.py`, that uses the module to process a sample log file.
* Display the results in a clear, readable format when the script is executed.

### Instructions

Create a file named `log_processor.py` containing three separate functions:

* One that returns the total number of lines in a file.
* One that returns the total number of words.
* One that returns the total number of characters (including spaces).

Create a separate script named `analyze_logs.py`:

* Import the `log_processor` module.
* Define the log file path (e.g., `log.txt`).
* Call the module’s functions to analyze the log file.
* Print the total lines, words, and characters to the terminal.

### Sample Output

When run with the following log file (`log.txt`):

```
Frame 001 rendered successfully  
Frame 002 rendered successfully  
Frame 003 failed due to missing texture  
```

The output should be:

```
Total Lines: 3  
Total Words: 13  
Total Characters: 84  
```
