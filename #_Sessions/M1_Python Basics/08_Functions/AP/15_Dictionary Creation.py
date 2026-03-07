"""
# Description of the Task
Create a Python program that takes multiple key-value pairs as input from the user and stores them in a dictionary. 
The program should then print the resulting dictionary.

# Instructions
Prompt the user to enter the number of key-value pairs they want to input.
For each key-value pair, prompt the user to enter the key and the corresponding value.
Store these pairs in a dictionary.
Print the resulting dictionary.

# Learning Objective
Understand how to create and manipulate dictionaries in Python.
Practice taking user input and storing it in a dictionary.
Learn how to iterate and dynamically add items to a dictionary.

# Sample Usage

Enter the number of key-value pairs: 3
Enter key 1: name
Enter value for key 'name': John
Enter key 2: age
Enter value for key 'age': 25
Enter key 3: city
Enter value for key 'city': New York
Resulting Dictionary: {'name': 'John', 'age': 25, 'city': 'New York'}
"""

"""
Python program that takes multiple key-value pairs as input from the user and stores them in a dictionary. 
The program should then print the resulting dictionary."""


def dict_creation(number):

    # initialize empty dictinary
    user_dict ={}

    # loop to get each key value pair till the number of keys 
    for i in range(number):
        key =  input(f"Enter key {i+1}: ")
        value = input(f"Enter value for '{key}': ")

        user_dict[key] =value # add the input to dictinary 

    print("Resulting Dictionary:",user_dict)

# Ask the user how many key-value pairs they want to enter
user_input = int(input("How many key-value pairs do you want to enter? "))
dict_creation(user_input)

"""
How many key-value pairs do you want to enter? 3   
Enter key 1: Name
Enter value for 'Name': Peter Parker
Enter key 2: Age 
Enter value for 'Age': 27
Enter key 3: City
Enter value for 'City': Brooklyn,New York
Resulting Dictionary: {'Name': 'Peter Parker', 'Age': '27', 'City': 'Brooklyn,New York'}
"""