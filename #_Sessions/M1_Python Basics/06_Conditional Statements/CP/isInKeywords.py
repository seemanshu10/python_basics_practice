"""
Kyword check if two variables point to the same object in memory 

This Is Not the smae as ==, which checks if the values are the same .

"""

# Using is with Lists 

a = [1,2,3]
b = a

if a is b:
    print("a and b refers to the same object .")
else:
    print("a and b do not refers to the same object .")

# Output : a and b refers to the same object .

# Comparing Floats 
f1 = 0.1+0.2
f2= 0.3
if f1 is f2:
    print("Both 'f1' and 'f2' are the same object in memory.")
else: 
    print("They are the different object in memory.")

# Output : 
# They are the different object in memory.

# using is with dictionaries 
dict1 = {'name':'Alice','age':30}
dict2 = {'name':'Alice','age':30}

if dict1 is dict2:
    print("Both 'dict1' and 'dict2' are the same object in memory.")
else:
    print("They are the different object in memory.")

# Outoput: They are the different object in memory.

# In Keyword 

my_dict = {'name':'Alice','age':30}
if 'age' in my_dict:
    print("Key 'age' is present in the dictinary.")
else:
    print("Key 'age' is not present in the dictinary.")

# Output : Key 'age' is present in the dictinary.

# using in with a list Containing Integers and Floats 
numbers = [1,2,3.5,4.5,5]

if 3 in numbers:
    print("3 is in the list.")
else:
    print("3 is not in the list.")

if 3.5 in numbers:
    print("3.5 is in the list.")
else:
    print("3.5 is not in the list.")

# Output 
# 3 is not in the list.
# 3.5 is in the list.

# using is not with List 

x = [4,5,6]
y = [4,5,6]

if x is not y:
    print("x and y are not the same object.")
else:
    print("x and y are the same object.")
# Output
# x and y are not the same object.

# using is not with Dictinaries 
my_dict = {'name':'Alice'}
my_dict1 = {'name':'David'}
if my_dict is not my_dict1:
    print("my_dict and my_dict1 are not the same object.")
else:
    print("my_dict and my_dict1 are the same object.")

# outPut
# my_dict and my_dict1 are not the same object.