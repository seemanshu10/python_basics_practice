# if statement
number = 10

if number > 0:
    print("The number is positive.")


#  if-else - Statement
number = -3

if number > 0:
    print("The number is positive.")
else:
    print("The number is negative.")


# if-elif-else - Statement
age = 16

if age < 12:
    print("Child ticket: $10")
elif age < 18:
    print("Teen ticket: $15")
elif age < 65:
    print("Adult ticket: $20")
else:
    print("Senior ticket: $12")


# Nested if - Statements
weather = "sunny"  
has_umbrella = "no" 

if weather == "rainy":
    if has_umbrella == "yes":
        print("You can go outside without getting wet.")
    else:
        print("You might get wet. Stay indoors or find an umbrella!")
else:
    print("The weather is nice. You can go outside!")
