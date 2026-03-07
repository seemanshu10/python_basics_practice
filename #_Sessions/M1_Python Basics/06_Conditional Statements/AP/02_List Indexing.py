"""
# Description of the Task
Create a program that allows the user to access elements from a predefined list of colors based 
on the index provided by the user. 
The program should handle out-of-range indices gracefully by displaying an error message.

# Instructions
Define a list of colors.
Prompt the user to enter an index.
Print the color at the specified index.
If the index is out of range, print an error message.

# Learning Objective
Understanding how to define and work with lists in Python.
Practicing list indexing to access elements.
Implementing basic error handling for index out-of-range scenarios.
"""

"""
program that allows the user to access elements from a predefined list of colors based on the index provided by the user. 
The program should handle out-of-range indices gracefully by displaying an error message.
"""

# Define The List of colors 

colors = ['Blue','Green','Red','Black','White']
# user input 
color_name = str(input("Enter the color name:"))

# checking if the input is found 
if color_name in colors:
    index_colors = colors.index(color_name)
    print("Color found in colors:", index_colors)
else:
    print("Color not found in colors:")

# Output 
# Enter the color name:Black  
# Color found in colors: 3