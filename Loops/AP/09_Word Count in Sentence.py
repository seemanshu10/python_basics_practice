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
    # check if the word is already in dictinary count1  if not add in dict 
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word] =1

# print the results 
print(word_count)

"""
{'This': 2, 'is': 2, 'a': 1, 'test.': 1, 'test': 1, 'simple.': 1}
"""