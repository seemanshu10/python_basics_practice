"""
# Description of the Task
Write a Python program that takes two lists of integers from the user and finds the common elements between the two lists.

# Instructions
Prompt the user to input two lists of integers.
Convert the input strings into lists of integers.
Find the common elements between the two lists.
Print the common elements.

# Learning Objective
The objective of this task is to practice list manipulation, including reading user input, 
converting strings to lists, and finding intersections of lists.
"""

"""
program that takes two lists of integers from the user and finds the common elements between the two lists.
"""

#  user to enter the first list of numbers
list1_input = input("Enter the first list of numbers separated by spaces: ")
# Convert the input string to a list of integers
list1 = list(map(int, list1_input.split()))

#  user to enter the second list of numbers
list2_input = input("Enter the second list of numbers separated by spaces: ")
# Convert the input string to a list of integers
list2 = list(map(int, list2_input.split()))

# ctrating list of common numbers 
common_elements = []

# looping through list 1 
for numbers in list1:
    if numbers in list2 and numbers not in common_elements: # check if the number is in scond list,if it already in common_elemnets  
            common_elements.append(numbers)

# Print the common elements
print("Common elements:", common_elements)

"""
Enter the first list of numbers separated by spaces: 3 6 4 8 2 4 1
Enter the second list of numbers separated by spaces: 3 5 8 1 3 6 4
Common elements: [3, 6, 4, 8, 1]
"""