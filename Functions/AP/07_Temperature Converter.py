"""
Write a Python program that converts a temperature from Celsius to Fahrenheit and vice versa. The user should input the temperature and the conversion direction.
"""

# Defining Celsius To farenhiet 

def celsius_to_fahrenheit(celsius):

    """
    Converts Celsius to Fahrenheit

    Parameters : celsius

    returns : 
    Temp
    
    """
    return (celsius * 9/5) + 32

# Defining farenhiet to Celsius   

def fahrenheit_to_celsius(fahrenheit):

    """
    Converts Celsius to Fahrenheit

    Parameters : celsius

    returns : 
    Temp
    
    """
    return (fahrenheit * 9/5) + 32


def input_user():
    
    # print ing choices 
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    # taking Choice of Conversion 
    choice = input("Enter your choice (1/2): ")

    # checking which choice matches 
    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is {fahrenheit:.2f}°F")

    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is {celsius:.2f}°C")

    else:
        print("Invalid choice! Please enter 1 or 2.")
    
input_user()

"""
Temperature Converter
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
Enter your choice (1/2): 1
Enter temperature in Celsius: 36.6
36.6°C is 97.88°F

Temperature Converter
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
Enter your choice (1/2): 2
Enter temperature in Fahrenheit: 78
78.0°F is 172.40°C


"""