"""
# Task Description:
Create a function named calculate_bmi that calculates and returns the Body Mass Index (BMI) of a person based on their weight and height.

# Instructions:
Define a function named calculate_bmi that takes two arguments: weight (in kilograms) and height (in meters).
The function should return the BMI, which is calculated using the formula:
BMI=weightheight2BMI = \frac{weight}{height^2}BMI=height2weight​
Write another function named bmi_category that takes the BMI value as an argument and returns the category it falls into:
Underweight: BMI < 18.5
Normal weight: 18.5 <= BMI < 24.9
Overweight: 25 <= BMI < 29.9
Obesity: BMI >= 30

# Learning Objective:
Understand how to define and use functions in Python.
Learn how to perform arithmetic operations within functions.
Practice returning values from functions.
Use conditional statements to categorize numeric data.

Sample Usage and Expected Output:
# Example usage:
bmi = calculate_bmi(70, 1.75)
print(f"BMI: {bmi:.2f}")  # Expected output: BMI: 22.86
category = bmi_category(bmi)
print(f"Category: {category}")  # Expected output: Category: Normal weight
"""

"""
function named calculate_bmi that calculates and returns the Body Mass Index (BMI) of a person based on their weight and height.

"""
# creating The Functuion ()
def calculate_bmi(weight,height):
    """
    Calculate BMI Formula is BMI= {weight}{height^2}
    
    Parameters : Width , height 

    returns : 
    BMI
    """
    BMI = weight/(height**2)
    return BMI

def bmi_category(bmi):
    """
    Determine BMI category based on input 
    
    Parameters : Bmi

    returns : 
    category 
    """

    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Normal weight"
    else:
        return "Obesity"

def input_user():
    
    # Taking input from the user
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    # calling BMI 
    bmi = calculate_bmi(weight,height)

    # checking Category 
    category = bmi_category(bmi)

    # Print Category 
    print(f"Category: {category}")
    
input_user()

"""
Enter your weight in kilograms: 33 
Enter your height in meters: 6
Category: Underweight
"""