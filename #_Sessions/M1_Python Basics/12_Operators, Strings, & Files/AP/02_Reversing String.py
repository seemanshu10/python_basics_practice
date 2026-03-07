"""
🎯 AP. Reversing String

Task Objective
--------------
In this task, you will:
• Accept a string input from the user
• Apply string slicing techniques to manipulate text
• Extract a substring from the beginning of the input
• Skip characters using slicing with a step value
• Reverse the entire string using slicing


Instructions
------------
• Prompt the user to enter a word or phrase
• Use slicing to extract:
  - The first 4 characters from the string
  - Every second character in the string
  - The entire string in reverse order
• Print each of these results with a clear label

Sample Output
-------------
    Enter text: PythonProgramming
    First 4 chars: Pyth
    Every 2nd char: Pto rgamn
    Reversed: gnimmargorPnohtyP
"""

user_String = input("Enter the strings :")
user_String.strip()

print("First 4 chars: ",user_String[:4])
print("Every 2nd char: ",user_String[::2])
print("Reversed :",user_String[::-1])