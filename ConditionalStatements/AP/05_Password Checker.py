"""
program that takes a password as input from the user and checks if it meets the following criteria:
At least 8 characters long
Contains both uppercase and lowercase letters
Contains at least one numeric digit
"""

# Enter the user input Password 
password = input("Enter Your Password: ")

len_password = len(password)
has_upper = False
has_lower = False
has_digit = False

# check each character in the password 
for char in password:
    if char.isupper():
        has_upper=True
    elif char.islower():
        has_lower=True
    elif char.isdigit():
        has_digit=True

# check length 
is_longEnough = len(password)>=8

# validating all the conditions 
if is_longEnough and has_lower and has_upper and has_digit:
    print("Password is valid.")
else:
    print("Password is invalid.")
