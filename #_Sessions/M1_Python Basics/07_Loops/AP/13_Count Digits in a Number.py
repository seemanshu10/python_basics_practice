"""
# Description of the Task
Write a Python program that takes a number as input from the user and counts the number of digits in the number using a while loop.

# Instructions
Prompt the user to enter a number.
Use a while loop to count the number of digits in the number.
Print the total number of digits.

# Learning Objective
The objective of this task is to help beginners understand how to use a while loop for repetitive tasks and to manipulate and process numeric input.

# Sample Usage
Example Input:
Enter a number: 12345
Expected Output:
The number of digits in the number is: 5

Example Input:
Enter a number: 789
Expected Output:
The number of digits in the number is: 3
"""

"""
 program that takes a number as input from the user and counts the number of digits in the number using a while loop.
"""

# input number 

num = int(input("Input A Number: "))

# store The reversed num 
count = 0

# reverse the num using while 
while num > 0:
    count +=1  # increase count 
    num = num//10 # remove the last digit 

# Print The Count 
print ("Total Number of Digits:", count)

"""
Input A Number: 2354
Total Number of Digits: 4
"""