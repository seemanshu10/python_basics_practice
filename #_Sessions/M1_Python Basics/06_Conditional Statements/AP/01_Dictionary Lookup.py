"""
# Description of the Task
Create a program that initializes a dictionary with predefined key-value pairs. 
The program should then prompt the user to enter a key and search for this key in the dictionary. 
If the key exists, the program should print the corresponding value. If the key does not exist, 
the program should print an error message indicating that the key is not found.

# Instructions
Initialize a dictionary with some predefined key-value pairs.
Prompt the user to enter a key to search for in the dictionary.
Check if the key exists in the dictionary.
If the key exists, print the corresponding value.
If the key does not exist, print an error message.

# Learning Objective
This task aims to help beginners understand:
How to initialize and use dictionaries in Python.
How to access values using keys.
How to handle cases where a key does not exist in the dictionary.

# Sample Usage

Enter a key to search: apple
Value: A sweet red fruit
Enter a key to search: banana
Value: A long yellow fruit
Enter a key to search: pineapple
Error: Key not found in the dictionary
"""

"""
program that initializes a dictionary with predefined key-value pairs. 
The program should then prompt the user to enter a key and search for this key in the dictionary. 
If the key exists, the program should print the corresponding value. If the key does not exist, 
the program should print an error message indicating that the key is not found.
"""

# Creating a dictionary 
my_dict = {
    'apple':' A sweet red fruit',
    'banana':'A long yellow fruit',
    'grapes':'A sweet Green fruit'
}

# taking user input 
user_input = str(input("Enter a key to search:"))
# checking if user input exist in my_dict
if user_input in my_dict:
    print("Value:", my_dict[user_input])
else:
    print("Error:","Key Not Found in the dictionary.")
"""
Output
Enter a key to search:apple
Value:  A sweet red fruit

Enter a key to search:banana
Value: A long yellow fruit

Enter a key to search:pineapple
Error: Key Not Found in the dictionary.
"""