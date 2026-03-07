"""
# Description of the Task
Write a Python program that takes a string as input from the user and
 counts the number of vowels in the string using a for loop and if-else statements.

# Instructions
Prompt the user to enter a string.
Initialize a counter to zero.
Iterate through each character in the string using a for loop.
Use an if-else statement to check if the character is a vowel (a, e, i, o, u - both uppercase and lowercase).
If the character is a vowel, increment the counter.
After the loop, print the total count of vowels.

# Learning Objective
Understand how to use for loops to iterate through a string.
Learn how to use if-else statements to check conditions.
Practice working with strings and character comparisons.
Understand how to count occurrences of specific items in a collection.

# Sample Usage
Example Input:
Enter a string: Hello, how are you?
Expected Output:
Number of vowels: 7
"""

"""
program that takes a string as input from the user and
counts the number of vowels in the string using a for loop and if-else statements.
"""

# user to enter the string  
sentence = input("Enter a string : ")
# Initialize the counter
vowels  = 0

# iterate through each character  in string 
for char in sentence:
    # check char is a vowel 
    if char in 'aeiouAEIOU':
        vowels += 1 # increment 
print(f"Vowels in string:", vowels)

"""
Enter a string : I lovae this !
Vowels in string: 5
"""