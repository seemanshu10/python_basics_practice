"""
Angle Conversions
Task Objective
In this task, you will:

Use the math module to convert angles between degrees and radians.
Convert an angle from degrees to radians.
Convert an angle from radians to degrees.
Print the results of both conversions clearly.
Instructions
Import the math module.
Define an angle in degrees (e.g., 180).
Convert it to radians using math.radians().
Define an angle in radians (e.g., math.pi).
Convert it to degrees using math.degrees().
Print both conversion results in a readable format.

"""

import math


while True:
    try:
        angle_degrees = int(input("Enter Your Angle Degree : "))
        
        # Convert degrees to radians
        angle_radians = math.radians(angle_degrees)

        # Print the result
        print(f"{angle_degrees} degrees is equal to {angle_radians} radians.")

        # Define an angle in radians
        angle_radians_input = math.pi

        # Convert radians to degrees
        angle_degrees_converted = math.degrees(angle_radians_input)
        # Print the result
        print(f"{angle_radians_input} radians is equal to {angle_degrees_converted} degrees.")

    
        break

    except ValueError:
        print("Only Integer between 1 to 100 can be entred. ")
