"""
Converting User Input Data

Task Objective
--------------
In this task, you will:
• Receive user input for age, height, and activity status
• Perform explicit type conversions to convert string input into
  appropriate data types (int, float, bool)
• Apply implicit type conversion during arithmetic operations
• Format and display the converted data in a user-friendly output


Instructions
------------
• Prompt the user to enter:
  - Their age (as an integer)
  - Their height in meters (as a float)
  - Their activity status (respond with "yes" or "no")
• Convert each input to the correct data type using explicit
  conversion functions
• Calculate:
  - Age in months (age × 12)
  - Height in centimeters (height × 100)
• Use implicit type conversion where necessary during calculations
• Print a formatted summary showing all the converted values

"""

# Function to get valid integer input
def get_valid_age():
    while True:
        age_input = input("Enter your age (in years): ")
        try:
            age = int(age_input)  # Explicit conversion
            if age > 0:
                return age
            else:
                print("Age must be a positive number. Try again.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


# Function to get valid float input
def get_valid_height():
    while True:
        height_input = input("Enter your height (in meters): ")
        try:
            height = float(height_input)  # Explicit conversion
            if height > 0:
                return height
            else:
                print("Height must be a positive number. Try again.")
        except ValueError:
            print("Invalid input. Please enter a decimal number.")


# Function to get valid yes/no input
def get_valid_activity():
    while True:
        activity_input = input("Are you active? (yes/no): ").lower()
        if activity_input == "yes":
            return True
        elif activity_input == "no":
            return False
        else:
            print("Invalid input . Please enter 'yes ' or 'no '.")


# Get validated inputs
age = get_valid_age()
height = get_valid_height()
is_active = get_valid_activity()

# Calculations (implicit type conversion occurs automatically)
age_in_months = age * 12          
height_in_cm = height * 100       

# Display summary
print("\n--- User Summary ---")
print(f"Age: {age} years")
print(f"Age in months: {age_in_months} months")
print(f"Height: {height:.2f} meters")
print(f"Height in centimeters: {height_in_cm:.2f} cm")
print(f"Active status: {is_active}")

          


        
