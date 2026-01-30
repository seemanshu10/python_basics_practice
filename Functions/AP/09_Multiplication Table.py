"""
Write a Python program that prints the multiplication table 
of a given number using a for loop. The user will input the number for which they want the multiplication table.
"""

def multiply_table(number):

    """
    Prints the multiplication table of the given number from 1 to 10.
    """

    for i in range(1,11):
        result = number *i 
        print(f"{number} x {i} = {result}")

def input_user():
    
    # taking input of number 
    user_input = int(input("Enter a number to print its multiplication table:"))

    # calling function 
    multiply_table(user_input)
    
input_user()

"""
Enter a number to print its multiplication table:6
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 6
"""