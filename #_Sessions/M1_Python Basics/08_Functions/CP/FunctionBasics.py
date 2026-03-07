"""
Docstring for Functions.CP.FunctionBasics
"""

# Function to Print a Simple Goodbye Message

def say_goodBye():
    print("Goodbyes ! Have A great Day !")

# say_goodBye()

# Goodbyes ! Have A great Day !

# Function for Simple Addition 

def add_num():
    a =12
    b=23
    print("The Sum is ",a+b)

# add_num()

# The Sum is  35

# Function to Show a Count Down

def countdown():
    count = 5 
    while count >0:
        print(count)
        count -= 1
countdown()

"""
5
4
3
2
1
"""
# Function to Print Even Numbers from 1 to 10

def print_even_numbers():
    num =2 
    while num <=10:
        print(num)
        num+=2
print_even_numbers()

"""
2
4
6
8
10
"""

# Function with One Parameter and Argument

def greet(name):
    print(f"Hello ,{name}!")

greet("Alice")
# Hello ,Alice!

# Function with multiple Parameters and Arguments

def introduce(name,age,city):
    print(f"My name is {name}, I'm {age} years old, and I live in {city} . ")

introduce("Alice",25,"London")

# My name is Alice, I'm 25 years old, and I live in London .

