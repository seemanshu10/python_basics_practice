"""
Basic Math Operations
Task Objective
In this task, you will:

Use the math module to perform fundamental mathematical operations.
Calculate the square root of a number.
Calculate the factorial of a number.
Calculate the result of one number raised to the power of another.
Instructions
Import the math module.
Define a number and calculate its square root using math.sqrt().
Define a number and calculate its factorial using math.factorial().
Define a base and exponent, and calculate the power using math.pow().
Print the results of all three calculations in a readable format.

"""

# import math module 
import math

# Calculate the square root of a number
number_for_sqrt = 16
sqrt_result = math.sqrt(number_for_sqrt)

# Calculate the factorial of a number
number_for_factorial = 5
factorial_result = math.factorial(number_for_factorial)

# Calculate one number raised to the power of another
base = 3
exponent = 4
power_result = math.pow(base, exponent)

# Print the results 
print(f"The square root of {number_for_sqrt} is {sqrt_result}")
print(f"The factorial of {number_for_factorial} is {factorial_result}")
print(f"{base} raised to the power of {exponent} is {power_result}")