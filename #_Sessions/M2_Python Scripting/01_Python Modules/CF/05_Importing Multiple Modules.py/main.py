from utilities.math import math_utils
from utilities.string import string_utils

result_add = math_utils.add(10, 5)
result_subtract = math_utils.subtract(10, 3)

uppercase = string_utils.to_uppercase("hello")
lowercase = string_utils.to_lowercase("WORLD")

print(f"Addition: {result_add}")   # Addition: 15
print(f"Subtraction: {result_subtract}")  # Subtraction: 7
print(f"Uppercase: {uppercase}")  # Uppercase: HELLO
print(f"Lowercase: {lowercase}")  # Lowercase: world