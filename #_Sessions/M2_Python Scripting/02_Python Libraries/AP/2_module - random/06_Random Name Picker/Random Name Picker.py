"""
Random Name Picker
Task Objective
In this task, you will:

Use the random module to select an item from a list.
Practice defining and working with string lists in Python.
Display information using basic print formatting.
Instructions
Import the random module.
Define a list containing several participant names.
Print all names in a readable format.
Use the random.choice() function to select a name from the list.
Print the selected name as the result.

"""

import random
list_ofNames = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

print("Welcomne to random Name picker ")

# join names with commas 
formatted_names = ", ".join(list_ofNames)
print(f"Participants: {formatted_names}" )

choice_rand = random.choice(list_ofNames)
print("The selected name is:",choice_rand)