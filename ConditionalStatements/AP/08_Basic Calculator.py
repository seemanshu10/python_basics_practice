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