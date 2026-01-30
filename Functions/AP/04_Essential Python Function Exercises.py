"""
This practice task involves creating several functions and a lambda function in Python to cover different concepts such as docstrings, multiple arguments, default arguments, lambda functions, positional and keyword arguments, returning multiple values, using one function within another, and higher-order functions.
Function with Docstring 
Function with Multiple Arguments
Function with Default Argument 
Lambda Function 
Function with Positional and Keyword Arguments 
Function Using Another Function 
Higher-Order Function 


Instructions : 

Write a function greet that takes a name as an argument and prints a greeting message. Include a docstring that describes what the function does.
Write a function add_numbers that takes two arguments and returns their sum. Include a docstring that describes what the function does.
Write a function introduce that takes two arguments: name and age, with age having a default value of 18. The function should print a message introducing the person.
Write a lambda function that takes two arguments and returns their product. Assign this lambda function to a variable multiply and use it to multiply two numbers.
Write a function describe_pet that takes a pet's name (positional argument) and an optional keyword argument animal_type with a default value of 'dog'. The function should print a message describing the pet.
Write a function rectangle_properties that takes the length and width of a rectangle and returns its area and perimeter.
Write a function circle_area that takes the radius of a circle and returns its area. Then write another function cylinder_volume that uses circle_area to calculate the volume of a cylinder given its radius and height.
Write a function apply_function that takes another function and a value as arguments, and returns the result of applying the given function to the value. Test it with a lambda function.

"""

def greet(name):
    """
    Prints a greeting message for the given name.
    """
    print(f"Hello, {name}!.")

# add function 
def add_numbers(a, b):
    """
    add numbers  
    
    Parameters : a,b (numbers)

    returns : 
    a+b
    """
    
    return a + b

def introduce(name, age=18):
    """
    Introduces a person with name and age.

    Parameters : name,age(defaultValue)

    returns : 
    None
    """
    print(f"My name is {name} and I am {age} years old.")


def describe_pet(name, animal_type="dog"):
    """
    Prints information about a pet.

    Parameter : name (Positional Argument) , animal_type (Keyword argument)

    returns : 
    None 
    """
    print(f"I have a {animal_type} named {name}.")

def rectangle_properties(length, width):
    """
    Returns the area and perimeter of a rectangle.

    Parameter : length,width (Positional Argument) 

    returns : 
    area, perimeter

    """
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def circle_area(radius):
    """
    Parameter : radius (Positional Argument) 

    Returns the area of a circle.
    """
    pi = 3.14159
    return pi * radius ** 2


def cylinder_volume(radius, height):
    """
    Parameter : radius,height (Positional Argument) 

    Returns :
    the volume of a cylinder using circle_area.
    """
    return circle_area(radius) * height

# Calling Functions 
greet("Alice")
# Hello, Alice!.

# Function with Multiple Arguments: add_numbers Function
result = add_numbers(3,4)
print(result)

# 7

# Function with Default Argument: introduce Function
introduce("Bob")
introduce("Charlie", 25)

"""
My name is Bob and I am 18 years old.
My name is Charlie and I am 25 years old.
"""
# Function with Positional and Keyword Arguments: describe_pet Function
describe_pet("Buddy")
describe_pet("Whiskers", animal_type="cat")

"""
I have a dog named Buddy.
I have a cat named Whiskers.
"""
# Function Returning Multiple Values: rectangle_properties Function
area, perimeter = rectangle_properties(5, 3)
print(f"Area: {area}, Perimeter: {perimeter}")

# Area: 15, Perimeter: 16

# Function Using Another Function: circle_area and cylinder_volume Functions

print("Circle Area:", circle_area(7))
print("Cylinder Volume:", cylinder_volume(7, 10))

"""
Circle Area: 153.93791
Cylinder Volume: 1539.3790999999999
"""

# Lambda Function 