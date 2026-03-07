"""
# Description of the Task
Write a Python program that:
Creates a list of integers.
Sorts the list in ascending and descending order.
Prints both sorted lists.

# Instructions
Define a list of integers.
Use Python's built-in functions to sort the list in both ascending and descending order.
Print the sorted lists to the console.

# Learning Objective
By completing this task, you will learn how to:
Define and manipulate lists in Python.
Use sorting functions to arrange list elements in a specific order.
Understand the use of built-in list methods.
"""

list_Num = input("Enter the list of integers seperated by spaces : ")

num_list = list(map(int , list_Num.split()))

asc_sort = sorted(num_list)
print ("The Acsending Order :", asc_sort)

dsc_sort = sorted(num_list, reverse=True)
print("The Decssending Order :", dsc_sort)

"""
Enter the list of integers seperated by spaces : 3 1 88 4 2 6 4 
The Acsending Order : [1, 2, 3, 4, 4, 6, 88]
The Decsending Order : [88, 6, 4, 4, 3, 2, 1]
"""
