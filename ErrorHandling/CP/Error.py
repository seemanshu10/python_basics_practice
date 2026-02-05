"""
Docstring for ErrorHandling.CP.Error
"""
# File Not Found Error

try: 
    with open("non_existent_file.txt") as file :
        content = file.read()
except FileNotFoundError:
    print("Error : File Does not Exist ")

# Error : File Does not Exist 

# Handling Index Errors 

my_list = [1,2,3]

try:
    print(my_list[5])
except IndexError:
    print("Error: Index out of range. ")

# Error: Index out of range. 

# Handling Type Errors

try:
    result = '5' + 5
except TypeError:
    print("Error: Cannot Combine different data Types.")

# Error: Cannot Combine different data Types.

# Errors Attribute Errors

my_list = [1,2,3]

try:
    my_list.append('4')
    print(my_list.size())
except AttributeError:
    print("Error: 'list' object has no attributes 'size'.")

# Error: 'list' object has no attributes 'size'.

# Handling NameErrors

def example_function():
    try:
        print(value)
    except NameError:
        print("Error: Local variable refrenced before assignment.")

example_function()

# Error: Local variable refrenced before assignment.

# Handling IOError

try: 
    with open("read_only_file.txt","w") as file :
        content = file.write("Hello World!")
except FileNotFoundError:
    print("Error : File Does not Exist ")

# Handling Key Errors in Dictionaries

my_dict = {'name': 'Alice' , 'age' : 30}
try:
    print(my_dict['address'])
except KeyError:
    print("Error: Key Not found in the dictionary.")

# Error: Key Not found in the dictionary.

# def demonstrate_potential_error():
#     if True:
#     print("This line is wrong")
# try:
#     demonstrate_potential_error()
# except IndentationError:
#     print("Error: Local variable refrenced before assignment.")

# Handling Value and Zero Division Errors

# try:
#     value = int(input("Enter a number: "))
#     result = 10 / value
#     print("Result:", result)

# except ValueError:
#     print("Please enter a valid integer.")

# except ZeroDivisionError:
#     print("Cannot Divide by zero.")

"""
Enter a number: a
Please enter a valid integer.

Enter a number: 0
Cannot Divide by zero.
"""

# File Operations with Error Handling

# try:
#     filename = input("Enter the filename to read: ")
#     with open("read_only_file.txt","r") as file :
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("Error : File Does not Exist ")
# except IOError:
#     print("An Error Occurred while reading the file.")

# Handling Index and Key Errors

# my_list = [1,2,3]
# my_dict = {'a': 1, 'b' : 2}

# try:
#     index = int(input("Enter an index for the list: "))
#     print("List Value:", my_list[index])

#     key = input("Enter an key for the list: ")
#     print("Dictionary Value:", my_dict[key])
    
# except ValueError:
#     print("Please enter a valid integer index.")

# except IndexError:
#     print("Index out of range for the list.")

# except KeyError:
#     print("Key not found in the dictionary.")

"""
Enter an index for the list: 2
List Value: 3
Enter an index for the list: 5
Key not found in the dictionary.

Enter an key for the list: b
Dictionary Value: 2

Enter an key for the list: c
Key not found in the dictionary.
"""

# Handling Multiple Input Errors

try:
    number1 = float(input("Enter The first number: "))
    number2 = float(input("Enter The first number: "))
    quotient = number1 / number2
    print("Quotient:", quotient)

except ValueError:
    print("Invalid input . Please enter numeric values.")

except ZeroDivisionError:
    print("Division by zero is not allowed .")

"""
Enter The first number: 10
Enter The first number: 0
Division by zero is not allowed .

"""