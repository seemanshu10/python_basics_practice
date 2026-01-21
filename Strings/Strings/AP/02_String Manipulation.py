"""
In this task, you will write a Python program that takes a string input from the user and performs various string manipulations. Specifically, you will:
Print the string in uppercase.
Print the string in lowercase.
Print the string with the first letter of each word capitalized.
Print the string in reverse order.

"""

# Taking input

text = input("Enter the string: ")

# Print the string in uppercase
print("Uppercase:", text.upper())

# Print the string in lowercase
print("Lowercase:", text.lower())

# Print the string with first letter of each word capitalized
print("Title case:", text.title())

# Print the string in reverse order
print("Reversed:", text[::-1])