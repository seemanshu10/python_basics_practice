"""
# Description of the Task
The task is to take a string input from the user that contains multiple words separated 
by spaces and split this string into a list of words. The program should then print the list of words.

# Instructions
Prompt the user to enter a string with multiple words.
Split the string into individual words based on spaces.
Print the resulting list of words.

# Learning Objective
Understand how to take string input from the user.
Learn how to use the split() method to divide a string into a list of words.
Practice working with lists and basic string manipulation.

# Sample Usage
Enter a sentence: The quick brown fox jumps over the lazy dog
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

"""

# Taking input

text = input("Enter the string: ")
print (text.split(" "))

