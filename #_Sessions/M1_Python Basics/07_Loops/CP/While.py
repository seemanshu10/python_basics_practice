"""
Docstring for Loops.CP.While
"""

# using While For Summing Numbers 

num = 1
total_sum = 0

while num <=10:
    total_sum+=num
    num+=1

print("Sum of num form 1 to 10 is:",total_sum)

# Sum of num form 1 to 10 is: 55

# using A while loop to validate User 
user_input = -1
while user_input<=0:
    user_input=int(input("Enter a Positive number:"))
print("You Entred: ",user_input)

"""
Enter a Positive number:-5
Enter a Positive number:9
You Entred:  9
"""

# iterating over a string 

text = "Hello"
index = 0
while index <len(text):
    print(text[index])
    index+=1
print("All Characters Printed :")

"""
H
e
l
l
o
All Characters Printed :
"""

# interating over Lists
text = [10,55,69,7,1]
index = 0
while index <len(text):
    print(text[index])
    index+=1
print("All numbers  Printed .")

"""
10
55
69
7
1
All numbers  Printed .
"""

# iterating over dict keys 
student_grades = {
    'Alice':85,
    'Bob':90
}
keys= list(student_grades.keys())

index =0
while index<len(keys):
    key =keys[index]
    print(key)
    index+=1

print("All Keys printed.")

# iterating over dict keys and values 
student_grades = {
    'Alice':85,
    'Bob':90,
    'David':55
}
keys= list(student_grades.keys())

index =0
while index<len(keys):
    key =keys[index]
    value=student_grades[key]
    print(f"{key}:{value}")
    index+=1

print("All grades  printed.")

"""
Alice:85
Bob:90
David:55
All grades  printed.
"""

# flattening a matrix 

matrix = [
    [1,2,1],
    [5,2,3],
    [7,8,9]
]

flattened = []
for row in matrix:
    for item in row:
        flattened.append(item)

print(flattened)

# [1, 2, 1, 5, 2, 3, 7, 8, 9]

# Generating multiplaction table 

size = 4 

i= 1
while i<=size:
    j=1
    while j <=size:
        print(i*j,end='\t')
        j+=1
    print()
    i+=1
"""
1       2       3       4
2       4       6       8
3       6       9       12
4       8       12      16
"""

# printing inverted traingle 

height = 5

i=height
while i >0:
    j=0
    while j <i:
        print('*',end=' ')
        j+=1
    print()
    i-=1
"""
* * * * *
* * * *
* * *
* *
*
"""

# printing a number Pattern 

rows = 5
current_row =1

while current_row <= rows:
    current_col =1

    while current_col <=current_row:
        print(current_col,end=' ')
        current_col+=1
        
    print()
    current_row+=1
print("All Rows Printed.")

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
All Rows Printed.
"""

# Generating combinations of two lists 

fruits = ["Apple","Banana","Cherry"]
colors = ["Red","Yellow","Pink"]

fruit_index = 0
while fruit_index < len(fruits):
    color_index =0
    while color_index <len(colors):
        print(f"{fruits[fruit_index]}-{colors[color_index]}")
        color_index+=1
    fruit_index+=1
print("All Combinatins Printed.")

"""
Apple-Red
Apple-Yellow
Apple-Pink
Banana-Red
Banana-Yellow
Banana-Pink
Cherry-Red
Cherry-Yellow
Cherry-Pink
All Combinatins Printed.
"""