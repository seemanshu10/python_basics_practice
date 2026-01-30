"""
Docstring for Functions.CP.Scope
"""

# Reading global variable 

message = "Hello World! "
def print_message():
    print(message)
print_message()

# Hello World! 

# Reading Global Variable with Conditional Logic

threshold = 10

def check_value(value):
    if value > threshold:
        print("Value is above the threshold.")
    else:
        print("Value is below or equal to the threshold.")

check_value(15)
check_value(5)

"""
Value is above the threshold.
Value is below or equal to the threshold.
"""

# Using Global Variable for Configuration

config = "development"

def display_config():
    print(f"Corrent configuration: {config}")

display_config()

# Corrent configuration: development

# Calculating with Global Variable

multiplier =2 

def calculate_product(value):
    product = value * multiplier
    print(f"Product:{product}")

calculate_product(5)

# Product:10

# Basic Local Variable Declaration

def greet():
    greeting = "Hello World!"
    print(greeting)

greet()

# Hello World!