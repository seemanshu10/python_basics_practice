"""
If Statements 
"""

# Checking If Number is Equal 
number = 100
if number == 100:
    print("The Number is 100.")

# Output : The Number is 100.

# Checking is a string is Hello 
greet = "Hello"
if greet=="Hello":
    print("The greeting is Hello.")
# Output : The greeting is Hello.

# Checking greater than 
number = 75 
if number>50:
    print("The Number is greater than 50.")
# Output : The Number is greater than 50.

# Check If Temp is above freezing 
temp = 10
if temp >0:
    print("The temp is above freezing.")
# output : The temp is above freezing.

# if else Statement 
# check if a number is even or odd 
number = 8
if number%2==0:
    print("The Number is even.")
else:
    print("The Number is odd.")
# Output : The Number is even.

# checking if a string contains "Python"
text = "I love Python"
if "Python" in text:
    print("The Text Contains 'Python'.")
else:
    print("The Text Does not contain 'Python'.")
# Output : The Text Contains 'Python'.

# Checking if temp is hot or cold 
temp =30
if temp >25:
    print("it is Hot Outside.")
else:
    print("it is Cold Outside.")
# output : it is Hot Outside.

# if elif - statemnet 
# checking Temp Ranges 
temp = 22

if temp <0:
    print("It's Freezing.")
elif temp <10:
    print("It's Very cold.")
elif temp <20:
    print("It's Cool.")
elif temp <30:
    print("It's Warm.")
else:
    print("It's Hot . ")
# ourput : It's Warm.

# checking User Age For Discounts 
age = 22

if age <12:
    print("Child Ticket : $10")
elif age <18:
    print("Teen Ticket : $15")
elif age <65:
    print("Adult Ticket : $20")
else:
    print("Senior ticket: $12")
# ourput : Adult Ticket : $20

# check if Number is Psoitive , negative , or zero 
number = float(input("Enter A number: "))

if number >0:
    print("The Number is Positive.")
elif number < 0:
    print("The Number is Negative.")
else:
    print("The Number is Zero. ")

# OutPut 1 : 
# Enter A number: 5
# The NUmber is Positive.

# OutPut 2 : 
# Enter A number: -3
# The Number is Negative.

# OutPut 3 : 
# Enter A number: 0
# The Number is Zero.


