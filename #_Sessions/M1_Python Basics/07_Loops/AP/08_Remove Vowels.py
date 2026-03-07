"""
# Description of the Task
Create a Python program that removes all vowels from a given string input by the user and prints the modified string.

# Instructions
Prompt the user to enter a string.
Define the vowels (a, e, i, o, u) in both uppercase and lowercase.
Remove all vowels from the string.
Print the modified string without vowels.

# Learning Objective
This task aims to help beginners understand:
String manipulation techniques.
Looping through characters in a string.
Using conditionals to filter out specific characters.
String concatenation.

# Sample Usage

Enter a string: Hello World
Modified string: Hll Wrld
"""

"""
program that removes all vowels from a given string input by the user and prints the modified string.

"""
# enter a userInput 
user_Input = input("Enter A string : ")

# vowels Definition
vowels = "aeiouAEIOU"

# create empty string to store the result 
without_vowels_str = ""
# loop each characrted and check if it is vowels i not add in result if is skip it 

for char in user_Input:
    if char not in vowels:  # check if vowels 
        without_vowels_str += char

# print the result 
print("Strings Without Vowels:", without_vowels_str)

"""
Enter A string : I love this Python.
Strings Without Vowels:  lv ths Pythn.

Enter a string: Hello World
Modified string: Hll Wrld
"""