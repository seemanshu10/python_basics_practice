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
nums =map(int,split_num)

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