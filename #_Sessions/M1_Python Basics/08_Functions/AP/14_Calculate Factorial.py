"""
# Description of the Task
Write a Python program that calculates the factorial of a number entered by the user using a for loop. 
The factorial of a non-negative integer 𝑛n is the product of all positive integers less than or equal to 𝑛n. 
It is denoted by 𝑛!n!. For example, 5!=5×4×3×2×1=1205!=5×4×3×2×1=120.

# Instructions
Prompt the user to enter a non-negative integer.
Use a for loop to calculate the factorial of the number.
Print the calculated factorial.

# Learning Objective
This task helps beginners understand:
How to use for loops in Python.
How to handle user input.
Basic arithmetic operations.
The concept of factorials in mathematics.

# Sample Usage
Example Input:
Enter a non-negative integer: 5
Expected Output:
The factorial of 5 is 120

Example Input:
Enter a non-negative integer: 0
Expected Output:
The factorial of 0 is 1
"""

"""
Write a Python program that calculates the factorial of a number entered by the user using a for loop. 
Prompt the user to enter a non-negative integer.
Use a for loop to calculate the factorial of the number.
Print the calculated factorial.
"""

def factorial(n):
    """
    Returns the factorial of a non-negative integer n.
    """
    if n < 0:
        return None  # Factorial is not defined for negative numbers

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Prompt the user for input for non negative number 
num = int(input("Enter a non-negative integer: "))

# Calling function
fact = factorial(num)
# Print the result
if fact is None:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {fact}")


"""
Enter a non-negative integer: 5
The factorial of 5 is 120

Enter a non-negative integer: 0
The factorial of 0 is 1

Enter a non-negative integer: -1
Factorial is not defined for negative numbers.

"""