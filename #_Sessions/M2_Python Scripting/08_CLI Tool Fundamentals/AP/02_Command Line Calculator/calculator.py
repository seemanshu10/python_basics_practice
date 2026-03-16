import sys

if len(sys.argv) < 4:
    print("Usage: python Calculator.py  ")

else:
    number1 = float(sys.argv[1])
    number2 = float(sys.argv[3])
    operator = sys.argv[2]

    if operator == '+':
        print(f"Result: {number1 + number2} ")
    elif operator == '-':
        print(f"Result: {number1 - number2} ")
    elif operator == '*':
        print(f"Result: {number1 * number2} ")
    elif operator == '/':
        if number2 !=0:
            print(f"Result: {number1 / number2} ")
        else:
            print("Error: Division by zero ")

    else:
        print("Invalid Operator! USe + - * / ")

"""
python calculator.py 5 + 3 
Result: 8.0 

 python calculator.py 5 / 0 
Error: Division by zero 

python calculator.py 5 / 2 
Result: 2.5

python calculator.py 5 * 2
Result: 10.0
"""