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