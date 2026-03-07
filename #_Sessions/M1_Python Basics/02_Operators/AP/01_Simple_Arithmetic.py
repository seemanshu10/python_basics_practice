"""
# Description of the Task
Create a Python program that prompts the user to input two numbers and then computes and displays the sum, difference, product, and quotient of these numbers.

# Instructions
Prompt the user to input the first number.
Prompt the user to input the second number.
Calculate the sum of the two numbers.
Calculate the difference between the two numbers.
Calculate the product of the two numbers.
Calculate the quotient of the two numbers.
Display the results of each calculation.

# Learning Objective
To understand and use basic arithmetic operations in Python.
To practice taking user input and converting it to appropriate data types.
To learn basic output formatting in Python.
"""

##################################################
#prompts the user to input two numbers and then computes and displays the sum, difference, product, and quotient of these numbers.
##################################################

# taking user input 
number1 = int(input("Enter The first Number: "))
number2 = int(input("Enter The Second Number: "))

print ("\nFirst Number entred is:",number1)
print ("First Number entred is:",number2)

# adding the Numbers 
sum_ofNumbers = number1 + number2
print ("\nSum of Numbers is : ",sum_ofNumbers)

# subtracting the numbers  
differnce_ofNumbers = number1 - number2
print("\nDifference of Numbers is :", differnce_ofNumbers)

# Multiply the numbers 

product_ofNumbers = number1 * number2
print("\nProduct of Numbers is:", product_ofNumbers)

# dividing the numbers 
if number2 != 0:
    quotient_ofNumbers = number1 / number2
    print("\nQuotient of Numbers is:", quotient_ofNumbers)
else:
    print("\nQuotient of Numbers is: Cannot divide by zero")
