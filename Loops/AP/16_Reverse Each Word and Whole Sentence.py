"""
Reversing Each Word and Whole Sentence

### Task Objective

In this task, you will:
* Practice logic building using loop-based string reversal.
* Strengthen your understanding of how loops can manipulate text at the character level.
* Develop two types of output: word-wise reversed and full-sentence reversed.


### Instructions
* Accept a sentence input from the user.
* Split the sentence into words.
* Reverse each word individually using loop logic.
* Combine the reversed words while keeping the word order unchanged and print the result.
* Then, reverse the **entire sentence** character by character using a loop and print that as a second result.
    > Do **not** use `[::-1]`, `reversed()`, or other built-in functions
"""

# Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Reverse each word individually
#print("Each word reversed:", end=" ")
reversed_each_words = ""
# loop to take each word 
for word in words:
    reversed_words = ""
    # loop to take each char in a word   
    for char in word:
        reversed_words = char + reversed_words 
        
    reversed_each_words = reversed_each_words + " " +reversed_words

print("Each word reversed:", reversed_each_words )

# Reverse the entire sentence character by character
reversed_sentence = ""

for char in sentence:
    reversed_sentence = char + reversed_sentence

print("Entire sentence reversed:", reversed_sentence)

"""
Enter a sentence: Python is fun 
Each word reversed: nohtyP si nuf 
Entire sentence reversed: nuf si nohtyP

"""