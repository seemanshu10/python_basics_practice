"""
# Description of the Task
Create a simple calculator program that can perform basic arithmetic operations (addition, subtraction, multiplication, and division) using functions. The program will take two numbers and an operator as input and then call the appropriate function to perform the calculation and display the result.

# Instructions
Define four functions for the arithmetic operations: add(a, b), subtract(a, b), multiply(a, b), and divide(a, b).
Each function should take two arguments and return the result of the arithmetic operation.
Create a main function that:
Asks the user to input two numbers.
Asks the user to choose an operation (addition, subtraction, multiplication, or division).
Calls the corresponding function based on the user's choice.
Displays the result of the calculation.
Ensure the division function handles division by zero appropriately.

# Learning Objective
Understand how to define and call functions in Python.
Learn how to pass arguments to functions and return values from functions.
Practice handling user input and making decisions based on that input.

# Sample Usage
Enter the first number: 10
Enter the second number: 5
Choose an operation (+, -, *, /): +
The result of 10 + 5 is 15
"""

"""
simple calculator program that can perform basic arithmetic operations (addition, subtraction, multiplication, and division) using functions. The program will take two numbers and an operator as input and then call the appropriate function to perform the calculation and display the result.
"""

# arithmetic Operation 

# add function 
def add(a, b):
    return a + b

# Subtract func 
def subtract(a, b):
    return a - b

# multiply Function
def multiply(a, b):
    return a * b

# divide function
def divide(a, b):
    """
     divide two numbers 
    
    :param a: int
    :param b: int

    return
    float
    """
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b

def input_user():
    
    # Taking input from the user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    # Asking user to choose operation
    choice = input("Choose an operation (+, -, *, /): ")

    # Performing calculation based on choice
    if choice == "+":
        result = add(num1, num2)
        print(f"Result: {result}")

    elif choice == "-":
        result = subtract(num1, num2)
        print(f"Result: {result}")

    elif choice == "*":
        result = multiply(num1, num2)
        print(f"Result: {result}")

    elif choice == "/":
        result = divide(num1, num2)
        print(f"Result: {result}")

    else:
        print("Invalid choice!")
    
input_user()

"""
Enter first number: 25
Enter second number: 2
Choose an operation (+, -, *, /): /
Result: 12.5
"""