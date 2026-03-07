"""
# Description of the Task
Write a Python program that takes a string input from the user and counts the frequency of each 
character in the string. The program should then print the character frequencies.

# Instructions
Prompt the user to enter a string.
Count the occurrences of each character in the string.
Store the character counts in a dictionary, where keys are characters and values are their respective counts.
Print the dictionary containing character frequencies.

# Learning Objective
This task helps beginners understand how to:
Work with strings in Python.
Use dictionaries to store and retrieve data.
Iterate through strings.
Utilize conditional logic for counting occurrences.

# Sample Usage
Enter a string: hello world
Character frequencies:
h: 1
e: 1
l: 3
o: 2
 : 1
w: 1
r: 1
d: 1
"""

"""
 takes a string input from the user and counts the frequency of each 
character in the string. The program should then print the character frequencies.

"""

# Iser input of a string 

user_Input = input("Enter A string : ")

# Remove all spaces
user_Input = user_Input.replace(" ", "")

# create an empty dict to store character present in string 
char_freq={}

for char in user_Input:
    if char in char_freq:
        char_freq[char]+=1  # count increment if element exists and is added in dict 
    else:
        char_freq[char] =1  # creating key of char that exists but is new 

# Character frequency output 
print( "Character Frquencies are : ")
for char,freq in  char_freq.items():
    print(f"{char}:{freq}")

"""
Enter A string : Hello World To this Environment.  
Character Frquencies are : 
H:1
e:2
l:3
o:4
W:1
r:2
d:1
T:1
t:2
h:1
i:2
s:1
E:1
n:3
v:1
m:1
.:1
"""