# importing from multiple files in subfolders 

# from utilities.math_func import math_utils
# from utilities.strings_module import strings_utils

# addNum = math_utils.add(8,4)
# subNum = math_utils.sub(8,4)

# upperCaseStr = strings_utils.toLowerCase("WORLD")
# lowerCaseStr = strings_utils.toUpperCase("world")

# print(f"Addition: ",addNum)
# print(f"Subtract: ",subNum)
# print(f"UpperCase: ",upperCaseStr)
# print(f"LowerCase: ",lowerCaseStr)

"""
importing specific functions and multiple modules from modules 

"""

from utilities.math_func.math_utils import add,sub 
from utilities.strings_module import strings_utils

addNum = add(8,4)
subNum = sub(8,4)

upperCaseStr = strings_utils.toLowerCase("WORLD")
lowerCaseStr = strings_utils.toUpperCase("world")

print(f"Addition: ",addNum)
print(f"Subtract: ",subNum)
print(f"UpperCase: ",upperCaseStr)
print(f"LowerCase: ",lowerCaseStr)

"""
import everything with star
importing all files in module 

"""

# from utilities.math_func.math_utils import *
# from utilities.strings_module.strings_utils import *

# addNum = add(8,4)
# subNum = sub(8,4)

# upperCaseStr = toLowerCase("WORLD")
# lowerCaseStr = toUpperCase("world")

# print(f"Addition: ",addNum)
# print(f"Subtract: ",subNum)
# print(f"UpperCase: ",upperCaseStr)
# print(f"LowerCase: ",lowerCaseStr)

"""
importing modules function using aliases

"""

from utilities.math_func.math_utils import add,sub 
from utilities.strings_module import strings_utils as su #import with alias 

addNum = add(8,4)
subNum = sub(8,4)

upperCaseStr = su.toLowerCase("WORLD")
lowerCaseStr = su.toUpperCase("world")

print(f"Addition: ",addNum)
print(f"Subtract: ",subNum)
print(f"UpperCase: ",upperCaseStr)
print(f"LowerCase: ",lowerCaseStr)
