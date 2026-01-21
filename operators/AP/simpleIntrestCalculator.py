"""
calculates the simple interest for a given principal amount, rate of interest, and time period.

"""

# user input 
principle_Amount = float(input("Enter The Principle Amount: "))
rate_ofInterest = float(input("Enter The rate of intrest in percentage : "))
time_period = float(input("Enter The Time period in years! :"))

# calculating simple intrest 
simple_Interest = (principle_Amount*rate_ofInterest*time_period)/100

# print the result 
print ("Simple ientrest on Principal Amount: ",simple_Interest)
