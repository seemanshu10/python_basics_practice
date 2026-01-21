"""
Collect input for daily water consumption (in liters) over 3 days.
Calculate the average daily consumption.
Output the average and show the recommended limit for comparison.
"""

# user input for dailyintake (in litres) details 

waterConsumption_Day1 = float(input("Enter Water consumed on Day 1 (in litres):"))
waterConsumption_Day2 = float(input("Enter Water consumed on Day 2 (in litres):"))
waterConsumption_Day3 = float(input("Enter Water consumed on Day 3 (in litres):"))

# daily Limit set (litres) 
spending_Limit = float(input("Enter recommended Daily Water intake (in litres):"))

# calculating daily water consumption across three days . 
average_Consumption = (waterConsumption_Day1+waterConsumption_Day2+waterConsumption_Day3)/3

# displaying Results 
print ("\nAverage Daily Consumption:",average_Consumption,"litres")
print ("Recommended Limit: ",spending_Limit,"litres")
