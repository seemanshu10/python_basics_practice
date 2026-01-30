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