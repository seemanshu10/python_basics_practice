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
