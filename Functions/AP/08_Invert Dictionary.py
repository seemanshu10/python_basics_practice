"""
In this task, you will create a sample dictionary and then write a Python program to invert the dictionary, 
meaning the keys will become values and the values will become keys. 
This is useful in scenarios where you need to quickly look up keys based on their associated values.
"""

# function for inverting dictionaryy  

def invert_dictionary(dict):
    """
    Inverts a dictionary: keys become values and values become keys.
    
    param dict

    return dictionary
    """
    # create empty dictinary 
    inverted_dict = {} 

    for key,value in dict.items():
        inverted_dict[value] = key
    return inverted_dict


# passing Dictinary 
original_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
# calling function to invert dictionary 
inverted_dict = invert_dictionary(original_dict)
print("Original Dictionary:", original_dict)
print("Inverted Dictionary:", inverted_dict)

"""
Original Dictionary: {'a': 1, 'b': 2, 'c': 3}
Inverted Dictionary: {1: 'a', 2: 'b', 3: 'c'}
"""