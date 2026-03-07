"""
# Description of the Task
Write a Python program that takes a list of numbers as input from the user and counts how many of them
 are positive and how many are negative using a for loop and if-else statements.

# Instructions
Prompt the user to enter a list of numbers separated by spaces.
Convert the input string into a list of integers.
Initialize two counters, one for positive numbers and one for negative numbers.
Use a for loop to iterate through the list of numbers.
For each number, use an if-else statement to check if it is positive or negative.
Increment the respective counter based on the result of the check.
Print the counts of positive and negative numbers.

# Learning Objective
By completing this task, you will learn how to:
Accept user input and process it.
Use a for loop to iterate over a list.
Use if-else statements to perform conditional checks.
Count occurrences of specific conditions within a list.

# Sample Usage
Example Input:
Enter a list of numbers separated by spaces: 1 -2 3 -4 5 6 -7 8 -9 10

Expected Output:
Positive numbers: 6
Negative numbers: 4

"""

"""
program that takes a list of numbers as input from the user and counts how many of them
are positive and how many are negative using a for loop and if-else statements.
"""

# user to enter numbers with spaces 
numbers_input = input("Enter a list of numbers separated by spaces: ")

split_num=numbers_input.split()
# convert to list 
mainNum = map(int, split_num)
numbers = list(mainNum)

pos_Count= 0
neg_Count= 0

# Iterate through the list
for num in numbers:
    if num >= 0:
        pos_Count += 1
    else:
        neg_Count += 1

print("Positive Numbers: ", pos_Count)
print("Negative Numbers: ", neg_Count)