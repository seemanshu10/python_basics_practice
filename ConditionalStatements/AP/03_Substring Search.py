"""
Write a Python program that:
Takes two string inputs from the user: a main string and a substring.
Checks if the substring is present in the main string.
Prints the starting index of the substring if found, or a message indicating it is not found.

"""

# Taking input of a main String

main_string = str(input("Enter the string: "))
# taking The substring 
sub_string = str(input("Enter The Substring:"))

# checking the condition 
if sub_string in main_string:
    index = main_string.find(sub_string)
    print("Substring Found at index:",index)
else:
    print("Substring Not Found in the main string")

"""
Output

Enter the string: I love python.
Enter The Substring:love
Substring Found at index: 2
"""