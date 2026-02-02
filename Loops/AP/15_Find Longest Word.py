"""

### Task Objective

In this task, you will:
* Use loops to process words from a user-provided sentence.
* Apply string handling and conditional logic to find the longest word.
* Practice how to manage comparisons and store the best result during iteration.


### Instructions
* Prompt the user to enter a sentence containing multiple words.
* Split the sentence into words.
* Use a loop to iterate through all the words.
* Compare each word’s length to identify the longest one.
* After checking all words, print:
  * The longest word found.
  * Its length.
* If two or more words have the same length, print the first one that appears."""

# user input of String 

user_Input = input("Enter A sentence : ")

# convert the sentence into list of words by split 

words = user_Input.split()
print(words)

# Longest word 
longest_word = words[0]

# loop through all words 
for word in words:
    # compare Lengths of current longest word 
    if len(word) > len(longest_word):
        longest_word = word

# print the results 
print(" Longest word : ", longest_word)
print(" Length of the Longest word : ", len(longest_word))

"""
Enter A sentence : Python programming is both powerful and fun.
['Python', 'programming', 'is', 'both', 'powerful', 'and', 'fun.']
 Longest word :  programming
 Length of the Longest word :  11
"""