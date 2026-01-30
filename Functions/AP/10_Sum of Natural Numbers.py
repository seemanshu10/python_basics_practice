"""
Python program to calculate the sum of the first n natural numbers, where n is provided by the user.

"""

def multiply_table(number):

    """
    calculate the sum of the first n natural numbers, where n is provided by the user
    """
    sum = 0
    for i in range(number+1):
        sum += i 
    return sum

def input_user():
    
    # taking input of number 
    user_input = int(input("Enter a number to print natural numbers :"))

    # calling function 
    sum_num = multiply_table(user_input)
    print (f"The sum of the first {user_input} natural numbers is {sum_num}.")

input_user()

"""
Enter a number to print natural numbers :5
The sum of the first 5 natural numbers is 15.
"""