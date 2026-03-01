"""
Formatting Strings

Task Objective
--------------
In this task, you will:
• Accept a string input from the user
• Validate the string using built-in string methods:
  - Check if it contains only alphabetic characters
  - Check if it contains only numeric characters
  - Check if it is in title case
• Format and align the validation results using string alignment methods


Instructions
------------
• Prompt the user to enter a string
• Use the following string methods to validate properties:
  - isalpha()
  - isdigit()
  - istitle()
• Store the result of each validation in separate variables
• Format the output using alignment methods such as:
  - ljust()
  - rjust()
• Print a header and footer around the results
  for better visual clarity

"""

user_String = input("Enter the string :")
user_String=user_String.strip()

alpha = user_String.isalpha()
digit = user_String.isdigit()
title = user_String.istitle()

titleMain = "Validation Results:"
print("-"*40)
print(titleMain.center(40))
print("-"*40)

# Format and align output
print("Alphabetic".ljust(20), ":", str(alpha).rjust(6))
print("Numeric".ljust(20), ":", str(digit).rjust(6))
print("Title Case".ljust(20), ":", str(title).rjust(6))

# Footer
print("-" *40)