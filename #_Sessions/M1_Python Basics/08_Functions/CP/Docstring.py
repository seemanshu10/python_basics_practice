"""
Docstring for Functions.CP.Docstring
"""

def greet(name = "Guest"):
    """
    Display a  greet message 
    """

    print(f"Hello ,{name}!")

greet()
print(greet.__doc__)

# Display a  greet message

def add(a,b):
    """
    Calculate summ of two numbers 
    
    Parameters : 
    a (int or float ) : First Number
    b (int or float ) : Second Number 

    returns : 
    Float (sum)
    """
    
    return a+b

print(add.__doc__)

"""
Calculate summ of two numbers

    Parameters :
    a (int or float ) : First Number
    b (int or float ) : Second Number

    returns :
    Float (sum)
"""
help(greet)

"""
Help on function greet in module __main__:

greet(name='Guest')
    Display a  greet message
"""

def minimum(a,b):
    """Return True if the Number is even , otherwise false """
    return a if a < b else b

help(minimum)

"""
Help on function minimum in module __main__:

minimum(n)
    Return True if the Number is even , otherwise false
"""