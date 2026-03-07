"""
# Description of the Task
In this task, you will create a list of the first 20 natural numbers and generate a 
new list containing the squares of these numbers using list comprehension.

# Instructions
Create a list containing the first 20 natural numbers (i.e., numbers from 1 to 20).
Use list comprehension to create a new list where each element is the square of the corresponding element in the original list.
Print the new list of squared numbers.

# Learning Objective
The objective of this task is to practice creating and manipulating lists in Python. 
Specifically, you will learn how to use list comprehension, a concise and readable way to create lists based on existing lists.
"""

list_Num = input("Enter the list of integers seperated by spaces : ")

num_list = list(map(int ,list_Num.split()))
squared_list = [] 
for num in num_list: 
    squared = num **2
    squared_list.append(squared)
print(squared_list)