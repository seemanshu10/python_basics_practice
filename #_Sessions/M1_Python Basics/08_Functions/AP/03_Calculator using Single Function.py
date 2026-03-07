"""
# Description of the Task
Create a simple calculator function that performs basic arithmetic operations (addition, subtraction, multiplication, division).

# Instructions
Define a function calculator that takes three arguments: num1, num2, and operation.
The operation argument should be a string that specifies the operation to perform: "add", "subtract", "multiply", or "divide".
The function should return the result of the operation.

# Learning Objective
Understand how to define and call functions in Python.
Learn how to handle different operations based on input arguments.

# Sample Usage
print(calculator(10, 5, "add"))       # Output: 15
print(calculator(10, 5, "subtract"))  # Output: 5
print(calculator(10, 5, "multiply"))  # Output: 50
print(calculator(10, 5, "divide"))    # Output: 2.0
"""

"""
simple calculator function that performs basic arithmetic operations (addition, subtraction, multiplication, division).
"""
# calculator Function 
def calculator(num1, num2, operation):
    if operation == "add":
        return num1+num2

    elif operation == "subtract":
        return num1-num2

    elif operation == "multiply":
        return num1*num2

    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1/num2
    else:
        return "Error: Invalid operation"
print(calculator(10, 5, "add")) 
print(calculator(10, 5, "subtract"))
print(calculator(10, 5, "multiply"))
print(calculator(10, 5, "divide"))    

"""
15
5
50
2.0
"""