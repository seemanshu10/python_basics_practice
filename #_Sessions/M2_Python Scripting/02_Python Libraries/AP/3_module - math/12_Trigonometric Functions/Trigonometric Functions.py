"""
Trigonometric Functions
Task Objective
In this task, you will:

Use the math module to perform trigonometric calculations.
Calculate the sine, cosine, and tangent of a given angle in radians.
Display each result with proper formatting in the output.
Instructions
Write a Python script that performs the following operations using the math library:

Calculate the sine of a given angle (in radians).
Calculate the cosine of a given angle (in radians).
Calculate the tangent of a given angle (in radians).
Use the functions math.sin(), math.cos(), and math.tan() respectively.
Print the results for each operation.

"""

import math

value_ofDegree = 25

# calculating radians 
sine = math.sin(value_ofDegree)
cos = math.cos(value_ofDegree)
tan = math.tan(value_ofDegree)

# print the result 

print(f"The sine of {value_ofDegree} radians is {sine}")
print(f"The cosine of {value_ofDegree} radians is {cos}")
print(f"The tangent of {value_ofDegree} radians is {tan}")

"""
The sine of 25 radians is -0.13235175009777303
The cosine of 25 radians is 0.9912028118634736
The tangent of 25 radians is -0.13352640702153587
"""
