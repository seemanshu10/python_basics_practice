"""
Prompt the user to enter a list of numbers separated by spaces.
Convert the input string into a list of integers.
Initialize a variable to store the largest number found so far.
Use a for loop to iterate through the list of numbers.
Use an if-else statement to update the largest number whenever a larger number is found.
Print the largest number at the end.
"""

# user to enter numbers with spaces 
numbers_input = input("Enter a list of numbers separated by spaces: ")

split_num=numbers_input.split()
# convert to list 
numbers = list(map(int, split_num))

# Initialize the largest number
largest = numbers[0]

# Iterate through the list
for num in numbers:
    if num > largest:
        largest = num

# Print the result
print("The largest number is:", largest)

"""
Enter a list of numbers separated by spaces: 7 2 66 44 1 6
The largest number is: 66
"""