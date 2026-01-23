"""
list methods

"""

# adding a single item 

num = [] 
num.append(10)
print(num)

# output: [10]

# appending nested lists  
# append always adds elemnt to end of string 

nested_list = []

nested_list.append([1,2.5,"No"])
nested_list.append([3,True,2])
print(nested_list)
# output : [[1, 2.5, 'No'], [3, True, 2]]

# insert , can insert anywhere default is end , if no index provided 

# inserting in the middle of a list 

num = [1,2,3,89]
num.insert(2,68)
print(num) # Output : [1, 2, 68, 3, 89]

# inseting Multiple Times 

movies = ["Inception","Avatar"]

movies.insert(1,"Titanic")
print(movies)
# Output : ['Inception', 'Titanic', 'Avatar']
movies.insert(2,"Matrix")
print(movies)
# Output : ['Inception', 'Titanic', 'Matrix', 'Avatar'] 

ne = []

ne.insert(0,"No")
print(ne)
# output : ['No']

# Extend : 
# Extending with a list of Mixed Data types 

mixed_ls = [1,"Two",8.0]
more_ls = [4,"One","Three"]

mixed_ls.extend(more_ls)
print(mixed_ls)
# output [1, 'Two', 8.0, 4, 'One', 'Three']

# extending with a string 
chars = ['a','b']
chars.extend("cde")
print(chars)

# output : ['a', 'b', 'c', 'd', 'e']

# remove 
# pop 

# popping for mlist 
"""
empty_list = []
poped_item = empty_list.pop()
print (poped_item)


Traceback (most recent call last):
  File "d:\PipelineTD\python_basics_practice\Lists\ListMethods.py", line 72, in <module>        
    poped_item = empty_list.pop()
IndexError: pop from empty list
"""

# popping form index 

colors = ["red","Green","Blue","Yellow"]
index_ToPop = 3

print(colors.pop(index_ToPop))
print (colors)
# Output : Yellow
# ['red', 'Green', 'Blue']

# del Keyword 

# deleting Elemnet from nested List 
data = [
    [10,20.50,21],
    ["apple","banana"],
    [1.2,8.5,25]
]

del data[2]
print (nested_list)
# Output : [[1, 2.5, 'No'], [3, True, 2]]

# delete an entire list 

num = [1,3.4,6,8]
del num
print(num)

# index 

# specifying Start and End Indices 

grades = [90,456,566,12,45]
index1 = grades.index(566,3)
print (index1)