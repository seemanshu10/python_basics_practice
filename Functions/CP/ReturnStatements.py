"""
Docstring for Functions.CP.ReturnStatements
"""
# Sum of Two Numbers
def add_numbers(a,b):
    return a+b

result = add_numbers(5,9)
print(result)

# 14

# Returning a String Message

def welcome_message():
    return "welcome to python ! "

message = welcome_message()
print(message)

# welcome to python !

# Returning the First Item in a List

def first_items(items):
    return items[0]

result = first_items([10,21,852,12])
print(result)

# 10

# Factorial of number 

def factorial(n):
    result =1
    while n>1:
        result *=n
        n-=1
    return result

result = factorial(5)
print(result)

# 120

# sum Of List of Numbers 

def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

result = sum_of_list([5,10,15])
print(result)

# 30

# length if a string 
def string_length(s):
    return len(s)

result = string_length("Hello World!")
print(result)
# 12

# maximum of Two Numbers 

def maximum(a,b):
    if a>b:
        return a
    else:
        return b
    
result = maximum(10,20)
print(result)
# Output: 20

# Returning String Length and Uppercase
def string_info(s):
    return len(s),s.upper()

length, upperCase = string_info("Hello World!")
print(f"Length is: {length}, Uppercase is: {upperCase}")

# Length is: 12, Uppercase is: HELLO WORLD!

# Returning a Sum and Difference

def sumDiff(a,b):
    return a+b,a-b

result_sum,result_diff = sumDiff(10, 8)
print(f"Sum : {result_sum} , Difference : {result_diff} . ")

# Sum : 18 , Difference : 2 .

# Returning Coordinates

def get_cordinates():
    x=23
    y=20
    return x,y

x ,y = get_cordinates()
print(f"Cordinates: ({x},{y}) ")

# Cordinates: (23,20)

# Multiple Properties of a Rectangle

def rectangle_properties(length,width):
    area = length*width
    perimeter = 2*(length+width)
    return area,perimeter

area , perimeter = rectangle_properties(12, 6)
print(f"Area : {area} , Perimeter : {perimeter} . ")
# Area : 72 , Perimeter : 36 .

# Returning Status and Message

def check_value(value):
    if value >0:
        return "Positive","The Value is greater than zero."
    elif value <0:
        return "Negative","The Value is less than zero."
    else:
        return "Zero","The Value is zero."
    
status,message =check_value(10)
print(f"Status: {status} , Message : {message} . ")

# Status: Positive , Message : The Value is greater than zero. 

# Returning Full Name and Initials

def full_nameAnd_initials(firstName,lastName):
    full_name = f"{firstName}{lastName}"
    initials = f"{firstName[0]}{lastName[0]}"
    return full_name,initials

full_name, initials = full_nameAnd_initials("John","Doe")
print(f"Full_name: {full_name} , Initials : {initials} . ")

# Full_name: JohnDoe , Initials : JD .


