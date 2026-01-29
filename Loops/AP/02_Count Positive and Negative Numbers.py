"""
program that takes a list of numbers as input from the user and counts how many of them
 are positive and how many are negative using a for loop and if-else statements.
"""

# user to enter numbers with spaces 
numbers_input = input("Enter a list of numbers separated by spaces: ")

split_num=numbers_input.split()
# convert to list 
mainNum=map(int, split_num)
numbers = list(mainNum)

pos_Count= 0
neg_Count= 0

# Iterate through the list
for num in numbers:
    if num >= 0:
        pos_Count+= 1
    else:
        neg_Count+=1

print("Positive Numbers: ",pos_Count)
print("Negative Numbers: ",neg_Count)