"""
# Description of the Task
Write a Python program that:
Takes two string inputs from the user: a main string and a substring.
Checks if the substring is present in the main string.
Prints the starting index of the substring if found, or a message indicating it is not found.

# Instructions
Prompt the user to enter the main string.
Prompt the user to enter the substring.
Use Python string methods to determine if the substring is present in the main string.
If the substring is found, print the starting index of the first occurrence of the substring.
If the substring is not found, print an appropriate message.

# Learning Objective
The objective of this task is to practice working with Python strings, 
particularly string searching methods like find() or index(). 
This task helps in understanding how to manipulate and search within strings.

# Sample Usage
Enter the main string: Hello, welcome to the world of Python!
Enter the substring: welcome
Output: The substring 'welcome' is found at index 7.
"""

"""
Write a Python program that:
Takes two string inputs from the user: a main string and a substring.
Checks if the substring is present in the main string.
Prints the starting index of the substring if found, or a message indicating it is not found.

"""

# Taking input of a main String

main_string = str(input("Enter the string: "))
# taking The substring 
sub_string = str(input("Enter The Substring:"))

# checking the condition 
if sub_string in main_string:
    substring_index = main_string.find(sub_string)
    print("Substring Found at substring_index:", substring_index)
else:
    print("Substring Not Found in the main string")

"""
Output

Enter the string: I love python.
Enter The Substring:love
Substring Found at substring_index: 2
"""