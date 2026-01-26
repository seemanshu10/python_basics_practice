"""
 write a Python program that determines whether a number entered by the user is even or odd. This will help you practice basic input handling, conditionals, and modulo operations in Python.
"""

# Enter the user input 
number = int(input("Enter the number: "))

# checking odd or even 
if number%2==0:
    print("The Number is even.")
else:
    print("The Number is odd.")

"""
Enter the number: 3
The Number is odd.

Enter the number: 22
The Number is even
"""