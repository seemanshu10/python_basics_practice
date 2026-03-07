"""
Create a separate script named analyze_logs.py:

Import the log_processor module.
Define the log file path (e.g., log.txt).
Call the module’s functions to analyze the log file.
Print the total lines, words, and characters to the terminal.

"""

import log_processor 

LOGFILE_PATH = r"#_Sessions\M2_Python Scripting\01_Python Modules\AP\01_Data Processor Module\log.txt"

countLines = log_processor.countLines(LOGFILE_PATH)
print(f"Total Lines : {countLines}")

countWord = log_processor.countWords(LOGFILE_PATH)
print(f"Total Words : {countWord}")

countCharacters = log_processor.countcharacters(LOGFILE_PATH)
print(f"Total Characters (including spaces): {countCharacters}")
