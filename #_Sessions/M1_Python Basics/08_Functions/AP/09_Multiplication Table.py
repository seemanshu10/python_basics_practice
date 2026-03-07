"""
# Description of the Task: Write a Python program that prints the multiplication table 
of a given number using a for loop. The user will input the number for which they want the multiplication table.

# Instructions:
Prompt the user to enter a number.
Use a for loop to iterate from 1 to 10.
In each iteration, multiply the user's number by the current loop counter.
Print the result in the format "number x counter = result".

# Learning Objective:
Understand and implement basic input/output operations in Python.
Use for loops to iterate over a range of numbers.
Perform arithmetic operations within a loop.
Format and print output to the console.

# Sample Usage:
Enter a number: 5
Expected Output:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
"""

"""
Write a Python program that prints the multiplication table 
of a given number using a for loop. The user will input the number for which they want the multiplication table.
"""

def multiply_table(number):
    """
    Prints the multiplication table of the given number from 1 to 10.
    """
    for i in range(1,11):
        result = number *i 
        print(f"{number} x {i} = {result}")

def input_user():
    # taking input of number 
    user_input = int(input("Enter a number to print its multiplication table:"))

    # calling function 
    multiply_table(user_input)
    
input_user()

"""
Enter a number to print its multiplication table:6
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 6
"""