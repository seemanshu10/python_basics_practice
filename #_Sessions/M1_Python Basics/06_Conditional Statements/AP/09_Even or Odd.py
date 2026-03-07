"""
# Description of the Task
The goal of this task is to write a Python program that determines whether a number entered by the user is even or odd. This will help you practice basic input handling, conditionals, and modulo operations in Python.

# Instructions
Prompt the user to enter a number.
Read the input from the user.
Check if the number is even or odd using the modulo operator (%).
Print an appropriate message indicating whether the number is even or odd.

# Learning Objective
By completing this task, you will learn how to:
Accept user input in Python.
Convert input strings to integers.
Use conditional statements (if, else).
Use the modulo operator to determine the remainder of a division.
"""

"""
 write a Python program that determines whether a number entered by the user is even or odd. This will help you practice basic input handling, conditionals, and modulo operations in Python.
"""

# Enter the user input 
number = int(input("Enter the number: "))

# checking odd or even 
if number%2 == 0:
    print("The Number is even.")
else:
    print("The Number is odd.")

"""
Enter the number: 3
The Number is odd.

Enter the number: 22
The Number is even
"""