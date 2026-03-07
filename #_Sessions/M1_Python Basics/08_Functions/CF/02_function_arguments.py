# Position Arguments
def multiply(x, y):
    return x * y

result = multiply(2, 3)


# Keyword Arguments
def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")

greet(age=25, name="Alice")

# Default Arguments
def greet(name="World"):
    print(f"Hello, {name}!")

greet()
greet("Bob")