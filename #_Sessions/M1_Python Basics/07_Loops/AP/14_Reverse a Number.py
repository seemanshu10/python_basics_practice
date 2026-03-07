"""
# Description of the Task
In this task, you will write a Python program that takes a number as input from the user and prints its reverse. 
For example, if the user inputs 12345, the program should output 54321.

# Instructions
Prompt the user to enter a number.
Use a while loop to reverse the digits of the number.
Print the reversed number.

# Learning Objective
The objective of this task is to practice using while loops and basic arithmetic operations. You will also learn how to manipulate numbers and work with user input in Python.

# Sample Usage
Example Input:
Enter a number: 67890

Expected Output:
Reversed number: 09876
"""

"""
program that takes a number as input from the user and prints its reverse. 
For example, if the user inputs 12345, the program should output 54321.
"""
# input number 

num = int(input("Input A Number: "))

# store The reversed num 
reversed_num = 0

# reverse the num using while 
while num > 0:
    digit = num%10 # getting the last digit 
    reversed_num = reversed_num*10 + digit # adding the digit in reversed 
    num = num//10 # remove the last digit 

# print The Reversed order 
print("Reversed Number:", reversed_num)

"""
Input A Number: 25578
Reversed Number: 87552
"""