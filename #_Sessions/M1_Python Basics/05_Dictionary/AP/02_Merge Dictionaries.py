"""
# Description of the Task
In this task, you will create two dictionaries and merge them into a single dictionary. 
After merging, you will print the merged dictionary.

# Instructions
Create two dictionaries with some predefined key-value pairs.
Merge these dictionaries into a single dictionary.
Print the merged dictionary.

# Learning Objective
The objective of this task is to learn how to merge two dictionaries in Python and understand the behavior of key-value pairs when merging.

# Sample Usage
Suppose we have two dictionaries:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
After merging, the resulting dictionary should be:
{'a': 1, 'b': 3, 'c': 4}
"""

"""
create two dictionaries and merge them into a single dictionary. 
After merging, you will print the merged dictionary
"""

# Create Two Dictionaries 

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# using Updated Functions 

dict1.update(dict2)
print(dict1)
# Output : {'a': 1, 'b': 3, 'c': 4}
