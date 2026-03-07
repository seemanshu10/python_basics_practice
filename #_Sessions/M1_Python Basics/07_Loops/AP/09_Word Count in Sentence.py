"""
# Description of the Task
Create a Python program that counts the occurrences of each word in a sentence provided 
by the user and stores these counts in a dictionary.

# Instructions
Prompt the user to enter a sentence.
Split the sentence into words.
Count the occurrences of each word.
Store these counts in a dictionary where the keys are words and the values are the counts.
Print the dictionary.

# Learning Objective
The objective of this task is to practice:
String manipulation (splitting strings into words).
Using dictionaries to store and count occurrences of items.
Iterating over lists and updating dictionary entries.

# Sample Usage

Enter a sentence: This is a test. This test is simple.
{'This': 2, 'is': 2, 'a': 1, 'test.': 1, 'test': 1, 'simple.': 1}

"""

"""
program that counts the occurrences of each word in a sentence provided 
by the user and stores these counts in a dictionary.
"""

# user input of String 

user_Input = input("Enter A sentence : ")

# convert the sentence into list of words by split 

words = user_Input.split()

# create empty dixt to count the frequency 

word_count = {}

# loop through list check if word is new or not 
for word in words:
    if word in word_count:  # check if the word is already in dictinary count1 if not add in dict 
        word_count[word] += 1
    else:
        word_count[word] = 1

# print the results 
print(word_count)

"""
{'This': 2, 'is': 2, 'a': 1, 'test.': 1, 'test': 1, 'simple.': 1}
"""