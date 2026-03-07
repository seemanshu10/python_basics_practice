"""
# Description of the Task
Write a Python program that takes two string inputs from the user and checks 
if the two strings are anagrams of each other. An anagram is a word or phrase formed by 
rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Instructions
Prompt the user to enter two strings.
Check if the two strings are anagrams.
Print a message indicating whether the strings are anagrams or not.

# Learning Objective
This task aims to help beginners practice string manipulation, comparison, 
and basic use of sorting or counting techniques to determine if two strings are anagrams. 
It reinforces understanding of fundamental string operations and conditionals.

# Sample Usage
Enter the first string: listen
Enter the second string: silent
The strings are anagrams.


Enter the first string: hello
Enter the second string: world
The strings are not anagrams.
"""

# taking input from user 

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# If lengths differ, not anagrams
if len(str1) != len(str2):
    print("Not anagrams")
else:
    
    first_string = list(str1)
    second_string = list(str2)

    for ch in first_string:
        if ch in second_string:
            second_string.remove(ch)
        else:
            print("Not anagrams")
            break
    else:
        print("Anagrams")

