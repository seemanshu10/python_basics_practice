"""
# Description of the Task
Write a Python program to calculate the sum of the first n natural numbers, where n is provided by the user.

# Instructions
Prompt the user to enter a positive integer n.
Use a loop to calculate the sum of all natural numbers from 1 to n.
Print the sum.

# Learning Objective
Understand how to use loops to iterate over a range of numbers.
Practice using input to receive data from the user.
Learn to accumulate a total using a loop.

# Sample Usage

Enter a positive integer: 5
The sum of the first 5 natural numbers is 15.

"""

"""
Python program to calculate the sum of the first n natural numbers, where n is provided by the user.

"""

def multiply_table(number):
    """
    calculate the sum of the first n natural numbers, where n is provided by the user
    """
    sum = 0
    for i in range(number+1):
        sum += i 
    return sum

def input_user():
    
    # taking input of number 
    user_input = int(input("Enter a number to print natural numbers :"))

    # calling function 
    sum_of_num = multiply_table(user_input)
    print (f"The sum of the first {user_input} natural numbers is {sum_of_num}.")

input_user()

"""
Enter a number to print natural numbers :5
The sum of the first 5 natural numbers is 15.
"""