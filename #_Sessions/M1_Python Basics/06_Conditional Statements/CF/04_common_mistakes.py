# Overlooking Edge Cases
age = 0
if age > 18:
    print("You are an adult.")
else:
    print("You are not an adult.")


# Making Sure Data Types Are Right
user_input = "25"
if user_input > 18:
    print("You are an adult.")
else:
    print("You are not an adult.")


# Using Inefficient or Redundant Checks
temperature = 75
if temperature >= 70:
    if temperature < 80:
        print("Comfortable temperature.")


# Not Considering All Possible Conditions
score = 85
if score >= 90:
    print("Excellent")
elif score >= 80:
    print("Good")