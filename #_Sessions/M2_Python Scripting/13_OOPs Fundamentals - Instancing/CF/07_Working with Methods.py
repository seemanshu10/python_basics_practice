# ======================= METHODS WITH PARAMETERS & ARGUMENTS =======================

class Calculator:
    def add(self, a, b):  # a and b are parameters
        return a + b

calc = Calculator()             # Create object
result = calc.add(10, 5)        # Pass arguments
print(result)                   # Output: 15




# ======================= METHODS WITH NO ARGUMENTS =======================

class Greeter:
    def say_hello(self):
        print("Hello!")

g1 = Greeter()
g1.say_hello()




# ======================= METHODS WITH A SINGLE ARGUMENT =======================

class GreeterSingle:
    def say_hello(self, name):
        print(f"Hello, {name}!")

g2 = GreeterSingle()
g2.say_hello("Compositor")




# ======================= METHODS WITH DEFAULT ARGUMENT =======================

class GreeterDefault:
    def say_hello(self, name="Artist"):
        print(f"Hello, {name}!")

g3 = GreeterDefault()
g3.say_hello()
g3.say_hello("Lighter")




# ======================= METHODS WITH MULTIPLE ARGUMENTS =======================

class CalculatorMulti:
    def multiply(self, a, b, c):
        return a * b * c

calc2 = CalculatorMulti()
print(calc2.multiply(2, 3, 4))




# ======================= METHODS WITH *args =======================

class MathTool:
    def total(self, *args):
        return sum(args)

tool = MathTool()
print(tool.total(1, 2, 3))
print(tool.total(4, 5, 6, 7, 8))




# ======================= METHODS WITH **kwargs =======================

class UserSettings:
    def apply_preferences(self, **kwargs):
        print("Applying preferences:")
        for key, value in kwargs.items():
            print(f"{key} = {value}")

settings = UserSettings()
settings.apply_preferences(theme="dark", font_size=14, notifications=True)
