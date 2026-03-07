"""
# Description of the Task
Write a Python program to calculate the sum of all even numbers between 1 and 100 using a for loop and if-else statements.

# Instructions
Use a for loop to iterate through numbers from 1 to 100.
Use an if-else statement to check if a number is even.
If the number is even, add it to a running total.
Print the final sum after the loop completes.

# Learning Objective
Understand how to use for loops to iterate through a range of numbers.
Learn to use if-else statements to perform conditional checks.
Practice summing values using a running total within a loop.
Sample Usage (Example Usage and Expected Output)

# Sample usage
sum_of_even_numbers()
# Expected Output
Sum of even numbers between 1 and 100 is: 2550

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