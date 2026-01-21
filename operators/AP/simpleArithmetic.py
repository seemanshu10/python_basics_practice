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
