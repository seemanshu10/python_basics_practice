"""
# Description of the Task
In this task, you'll write a Python program that performs various operations on a list of numbers. You'll create a list, perform different operations like finding the largest and smallest numbers, calculating the sum of all numbers, and printing the list in reverse order.

# Instructions
Create a list of numbers (you can start with a predefined list or ask the user to input the numbers).
Print the list to the console.
Find and print the largest number in the list.
Find and print the smallest number in the list.
Calculate and print the sum of all numbers in the list.
Print the list in reverse order.

# Learning Objective
The objective of this task is to help beginners understand and practice the following Python concepts:
List creation and manipulation
Basic list operations (finding min, max, sum)
Looping through lists
Using built-in functions like max(), min(), and sum()
Reversing a list
"""


list_Num = input("Enter the list of integers seperated by spaces : ")

num_list = list(map(int , list_Num.split()))

print ("The list Entered is :" , num_list)
# output : The list Entered is : [1, 3, 9, 7, 2, 1]
max_num = max(num_list)
print ("MAX number is : ", max_num)

min_num = min(num_list)
print ("MIN number is : ", min_num)

sum_total = sum(num_list)
print ("SUM of list is : ", sum_total)
# output : The list Entered is : [3, 2, 122, 4, 6, 3, 1]
# MAX number is :  122
# MIN number is :  1
# SUM of list is :  141

rever_list = num_list[::-1]
print("Reversed list is :", rever_list)

# Reversed list is : [1, 3, 6, 4, 122, 2, 3]