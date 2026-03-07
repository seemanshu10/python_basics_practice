# Using Return 
def add_numbers(a, b):
    total = a + b 
    return total  

result = add_numbers(5, 3)


# example
def square(number):
    result = number * number
    return result 

output = square(4)


# Returning Multiple Value
def get_user_info():
    name = "Alice"
    age = 25
    return name, age  

user_name, user_age = get_user_info()

print("Name:", user_name)
print("Age:", user_age)  



# ------------------- Variable Scopes ---------------------

# Global Scope
x = 10 

def my_function():
    print("Inside function, x =", x)

my_function()

print("Outside function, x =", x)



# Local Scope 
def my_function():
    x = 5  # Local variable
    print("Inside function, x =", x)

my_function()

print(x)



# Using the global Keyword
x = 10 

print("Before Modification of x =", x)
def my_function():
    global x  
    x = 20  
    print("Inside function, x =", x)

my_function()

print("Outside function, x =", x)

