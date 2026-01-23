"""
nested list 
"""

# simple nested list 

nested_list= [
    ["Apple","Banana","Grapes"],
    ["dog","cat","Lion"],
    ["red","green","blue"],
    
]

print (nested_list)
# output : [['Apple', 'Banana', 'Grapes'], ['dog', 'cat', 'Lion'], ['red', 'green', 'blue']]

# mixed with numbers and strings and floats 

nested_list= [
    ["Apple",2,2.0],
    [80,2.8,"Lion"],
    ["red","green",9.9],
    
]

print (nested_list)

# output [['Apple', 2, 2.0], [80, 2.8, 'Lion'], ['red', 'green', 9.9]]

# nested list with strings and a 2d list 

nested_list= [
    "Apple","grapes",
    ["X","Y"],
    ["red","Blue"],
    
]

print (nested_list)
# [['Apple', 'Banana', 'Grapes'], ['dog', 'cat', 'Lion'], ['red', 'green', 'blue']]
#print (nested_list[1])

print (nested_list[2]) # grapes


# modyfying Nested List with strings and integers 

data = [
    [10,20.50,21],
    ["apple","banana"],
    [1.2,8.5,25]
]

print (data)
# [[10, 20.5, 21], ['apple', 'banana'], [1.2, 8.5, 25]]
data[0][2] = 99
print (data)
# [[10, 20.5, 99], ['apple', 'banana'], [1.2, 8.5, 25]]


# nested list with mixed data type 

mix_string = [
    ["Hello",False],
    [2.5,"No"]
]
print ("Original List: ")
print (mix_string)

mix_string[0][1] = True 
print ("New List: ")
print (mix_string)
"""
Original List:
[['Hello', False], [2.5, 'No']]
New List:
[['Hello', True], [2.5, 'No']]
"""
# nested list with boolean strings 

bool_string = [
    [True,False],
    ["Yes","No"]
]
print ("Original List: ")
print (bool_string)

bool_string[0][1] = True 
print ("New List: ")
print (bool_string)
"""
Original List:
[[True, False], ['Yes', 'No']]
New List:
[[True, True], ['Yes', 'No']]
"""

