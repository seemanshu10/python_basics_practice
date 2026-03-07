# --------------- Importing the Entire Module as Is --------------
import module1  

# Using a function from module1
module1.root_function()



# ------------ Importing Specific Functions from a Module --------------
from module1 import greet  

# Using the imported function
greet()



# ------------ Importing Multiple Functions from a Module --------------
from module1 import root_function, greet  

# Using the imported functions
root_function()
greet()



# ------------ Importing All Functions from a Module ------------------
from module1 import *  

# Using the imported function and variable
greet()
print(module_variable)



# --------------- Importing a Module with an Alias -----------------
import module1 as m4  

# Using the alias to call functions
m4.root_function()
m4.greet()



# --------------- Importing Modules Inside Folders with an Alias -----------
from func import module2 as m2

# Using the alias to call functions and variables
m2.func_function1()
print(m2.func_variable)

