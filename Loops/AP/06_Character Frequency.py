"""
 takes a string input from the user and counts the frequency of each 
character in the string. The program should then print the character frequencies.

"""

# Iser input of a string 

user_Input = input("Enter A string : ")
# removing Spaces 
# Remove all spaces
user_Input = user_Input.replace(" ", "")
# create an empty dict to store character present in string 
char_freq={}
for char in user_Input:
    if char in char_freq:
        # count increment if element exists and is added in dict 
        char_freq[char]+=1
    else:
        # creating key of char that exists but is new 
        char_freq[char] =1   

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