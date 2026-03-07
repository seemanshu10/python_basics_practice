"""# Description of the Task:
Write a Python program that calculates the simple interest for a given principal amount, rate of interest, and time period.

# Instructions:
Take input from the user for the principal amount, rate of interest (in percentage), and time period (in years).
Calculate the simple interest using the formula: 
Simple Interest=(Principal×Rate×Time)/100
Print the calculated simple interest

# Learning Objective:
Practice taking user input.
Apply mathematical calculations using Python.
Print the result to the console."""


# user input 
principle_Amount = float(input("Enter The Principle Amount: "))
rate_ofInterest = float(input("Enter The rate of intrest in percentage : "))
time_period = float(input("Enter The Time period in years! :"))

# calculating simple intrest 
simple_Interest = (principle_Amount*rate_ofInterest*time_period)/100

# print the result 
print ("Simple ientrest on Principal Amount: ",simple_Interest)