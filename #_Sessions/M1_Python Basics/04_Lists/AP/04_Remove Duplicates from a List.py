"""
# Description of the Task
Create a Python program that takes a list of integers from the user, removes any duplicate values, and prints the updated list.

# Instructions
Prompt the user to enter a list of integers separated by spaces.
Convert the input string into a list of integers.
Remove duplicate values from the list.
Print the updated list without duplicates.

# Learning Objective
This task aims to teach beginners how to:
Read input from the user.
Convert a string input to a list of integers.
Use set operations to remove duplicates from a list.
Iterate through a list and maintain order while removing duplicates.
Print the final list.
"""

# Take Input of a list from user 

list_Num = input("Enter the lsit of integers seperated by spaces : ")

# Covert the input string into a list of integers 
num_list = map(int , list_Num.split()) # list_
lis = list(num_list)
print (lis)
# Enter the lsit of integers seperated by spaces : 12 98 4 3 7 
# [12, 98, 4, 3, 7]

set_num = set(lis)
final_list = list(set_num)
print ("List without duplicated :  ", final_list)