"""
program that takes a string as input from the user and
counts the number of vowels in the string using a for loop and if-else statements.
"""

# user to enter the string  
sen = input("Enter a string : ")
# Initialize the counter
vowels  = 0

# iterate through each character  in string 
for char in sen:
    # check char is a vowel 
    if char in 'aeiouAEIOU':
        vowels+=1 # increment 
print(f"Vowels in string:",vowels)

"""
Enter a string : I lovae this !
Vowels in string: 5
"""