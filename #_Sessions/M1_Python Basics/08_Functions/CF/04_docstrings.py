# understanding DocString
def greet(name):
    """
    This function greets the person whose name is passed as a parameter.

    Parameters:
    name (str): The name of the person to greet.

    Returns:
    None
    """
    print(f"Hello, {name}!")



# ------------------ Accessing DocString -------------------

# Using __doc__ Attributes
print(greet.__doc__)


# Using - help() Function
def greet():
    """Display a greeting message."""
    print("Hello, World!")

help(greet)