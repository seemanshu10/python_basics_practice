"""
# Description of the Task
Write a Python program that takes a list of numbers as input from the user and finds the second largest number using a for loop and if-else statements.

# Instructions
Prompt the user to input a list of numbers.
Ensure the list contains at least two unique numbers.
Iterate through the list to find the largest and second largest numbers.
Print the second largest number.

# Learning Objective
Practice using for loops and if-else statements.
Understand how to handle and manipulate lists.
Learn how to find specific elements (second largest) in a list.

# Sample Usage
Example Input:
Enter numbers separated by spaces: 34 56 23 89 12 78 90 67
Expected Output:
The second largest number is: 89

Example Input:
Enter numbers separated by spaces: 5 3 9 7 2
Expected Output:
The second largest number is: 7
"""

"""
Prompt the user to input a list of numbers.
Ensure the list contains at least two unique numbers.
Iterate through the list to find the largest and second largest numbers.
Print the second largest number.
"""

# Prompt the user to enter numbers separated by spaces
numbers_input = input("Enter a list of numbers separated by spaces: ")

split_num = numbers_input.split(" ")
# map explitily converts to int of the split strings 
nums = map(int,split_num)

# Ensure there are at least two unique numbers in input 
unique_numbers = list(set(nums))
if len(unique_numbers) < 2:
    print("Error: You must enter at least two unique numbers.")
else:
    # Sort the unique numbers in descending order
    unique_numbers.sort(reverse=True)
    # The second largest is the second element of unique numbe
    second_largest = unique_numbers[1]
    
    print(f"The second largest number is: {second_largest}")