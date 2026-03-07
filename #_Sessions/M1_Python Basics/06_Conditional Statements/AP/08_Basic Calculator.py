"""# Description of the Task
Create a simple calculator program that performs basic arithmetic operations (addition, subtraction, multiplication, and division) based on user input.

# Instructions
Prompt the user to enter the first number.
Prompt the user to enter the second number.
Prompt the user to choose an operation (+, -, *, /).
Perform the chosen operation and display the result.
Handle cases where the user attempts to divide by zero by displaying an appropriate message.

# Learning Objective
This task aims to help beginners:
Understand how to take user input in Python.
Use basic arithmetic operators.
Implement conditional statements to perform different operations based on user input.
Handle exceptions such as division by zero.
Print output to the console.
"""

"""
 simple calculator program that performs basic arithmetic operations (addition, subtraction, multiplication, and division) based on user input.
"""

#user to enter the numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Choose an operation (+,-,*,/): ")

# choose the operation 

if operation == "+":
    print("Result: ",num1+num2)
elif operation == "-":
    print("Result: ",num1-num2)
elif operation == "*":
    print("Result: ",num1*num2)
elif operation == "/":
    if num2==0:
        print("Error: Division by zero is not allowed.")
    else:
        print("Result:",num1/num2)
else:
    print("Invalid operation selected.")
"""
Enter the first number: 225
Enter the second number: 0
Choose an operation (+,-,*,/): /
Error: Division by zero is not allowed. 

Enter the first number: 5
Enter the second number: 9
Choose an operation (+,-,*,/): /
Result: 0.5555555555555556

Enter the first number: 22 
Enter the second number: 12
Choose an operation (+,-,*,/): +
Result:  34.0
"""