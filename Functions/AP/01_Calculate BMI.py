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

    if bmi<18.5:
        return "Underweight"
    elif 18.5<=bmi<24.9:
        return "Normal weight"
    elif 25<=bmi<29.9:
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