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

# string Manipulation 
def convert_to_uppercase (text):
    upper_text =text.upper()
    print(upper_text)

convert_to_uppercase("hello, World!")

# HELLO, WORLD!

# Modifying a Global Variable

count = 0 

def incremnt():
    global count
    count += 1

incremnt()
incremnt()
print(count) # 2

# Using Global Variable in Multiple Function

total = 100

def add_to_total(amount):
    global total
    total+=amount

def subtrat_from_total(amount):
    global total
    total -= amount

add_to_total(50)
subtrat_from_total(20)
print(total)
# 130

# Global Variable for Game Score

score =0 

def increase_score(points):
    global score
    score+=points

def resetScore():
    global score
    score =0   
increase_score(50)
print("Score After increase: ",score)
resetScore()
print("Score Reset: ",score)

#Score After increase:  50
#Score Reset:  0

# Using Global variable or track state : 

is_running = False

def start_process():
    global is_running
    is_running =True
    print("Process Started.")

def stop_process():
    global is_running
    is_running =False
    print("Process Stopped.")

start_process()
print("Is Running . ", is_running)
stop_process()
print("Is Running . ", is_running)

"""
Is Running .  True
Process Stopped.
Is Running .  False
"""

