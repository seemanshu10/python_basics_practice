"""
# Description of the Task
Write a Python program that takes a number as input from the user and checks if it is divisible by 2, 3, or both using if-else statements.

# Instructions
Prompt the user to enter a number.
Check if the number is divisible by 2, 3, or both.
Print appropriate messages based on the divisibility.

# Learning Objective
The objective of this task is to practice using if-else statements for conditional checks
 and to understand the modulus operator (%) for determining divisibility.

# Sample Usage
Example 1:
Input: 6
Output: The number 6 is divisible by both 2 and 3.

Example 2:
Input: 4
Output: The number 4 is divisible by 2.

Example 3:
Input: 9
Output: The number 9 is divisible by 3.

Example 4:
Input: 7
Output: The number 7 is not divisible by 2 or 3.

"""

"""
Write a Python program that takes a number as input from the user and checks if it is divisible by 2, 3, or both using if-else statements.

"""

# Enter the user input 
number = int(input("Enter the number: "))

# Checking The divisibility 
if number%2==0 and number%3==0:
    print("The Number {} is divisible by both 2 and 3.".format(number))
elif number%2==0 :
    print("The Number {} is divisible by 2.".format(number))
elif number%3==0:
    print("The Number {} is divisible by 3.".format(number))
else:
    print("The Number {} is not divisible by 2 or 3.".format(number))

"""
Enter the number: 6
The Number 6 is divisible by both 2 and 3.

Enter the number: 4
The Number 4 is divisible by 2.

Enter the number: 9
The Number 9 is divisible by 3.

Enter the number: 7
The Number 7 is not divisible by 2 or 3.
"""