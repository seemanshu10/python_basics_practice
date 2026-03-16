import sys

if len(sys.argv) < 4:
    print("Usage: python mathOperation.py <number1> <operator> <number2>  ")

else:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[3])
    operator = sys.argv[2]

    if operator == '+':
        print(f"Result: {num1 + num2} ")
    elif operator == '-':
        print(f"Result: {num1 - num2} ")
    elif operator == '*':
        print(f"Result: {num1 * num2} ")
    elif operator == '/':
        if num2 !=0:
            print(f"Result: {num1 / num2} ")
        else:
            print("Error: Division by zero ")

    else:
        print("Invalid Operator! USe + - * / ")