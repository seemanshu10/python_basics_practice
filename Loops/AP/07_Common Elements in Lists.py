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
for num in list1:
    # check if the bumber is in scond list 
    if num in list2:
        # check if it slready in common_elemnets  
        if num not in common_elements:
            common_elements.append(num)

# Print the common elements
print("Common elements:", common_elements)

"""
Enter the first list of numbers separated by spaces: 3 6 4 8 2 4 1
Enter the second list of numbers separated by spaces: 3 5 8 1 3 6 4
Common elements: [3, 6, 4, 8, 1]
"""