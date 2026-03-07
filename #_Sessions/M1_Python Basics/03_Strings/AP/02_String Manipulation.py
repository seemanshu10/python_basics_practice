"""
# Description of the Task
In this task, you will write a Python program that takes a string input from the user and performs various string manipulations. Specifically, you will:
Print the string in uppercase.
Print the string in lowercase.
Print the string with the first letter of each word capitalized.
Print the string in reverse order.

# Instructions
Prompt the user to enter a string.
Print the string in uppercase using the upper() method.
Print the string in lowercase using the lower() method.
Print the string with the first letter of each word capitalized using the title() method.
Print the string in reverse order by slicing the string with [::-1].

# Learning Objective
The objective of this task is to help beginners understand and practice basic string manipulation methods in Python. By completing this task, you will learn how to:
Take user input.
Use different string methods to change the case of the text.
Use string slicing to reverse a string.
Print the manipulated strings to the console.
"""


# Taking input

text = input("Enter the string: ")

# Print the string in uppercase
print("Uppercase:", text.upper())

# Print the string in lowercase
print("Lowercase:", text.lower())

# Print the string with first letter of each word capitalized
print("Title case:", text.title())

# Print the string in reverse order
print("Reversed:", text[::-1])