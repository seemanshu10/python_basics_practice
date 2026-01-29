"""
program that takes a number as input from the user and prints its reverse. 
For example, if the user inputs 12345, the program should output 54321.
"""
# input number 

num = int(input("Input A Number: "))

# store The reversed num 
reversed_num = 0

# reverse the num using while 
while num >0:
    digit = num%10 # getting the last digit 
    reversed_num =reversed_num*10+digit # adding the digit in reversed 
    num = num//10 # remove the last digit 

# print The Reversed order 
print ("Reversed Number:",reversed_num)

"""
Input A Number: 25578
Reversed Number: 87552
"""