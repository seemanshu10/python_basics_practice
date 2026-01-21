"""
Task Objective:

• Accept user input for the quantity and unit price of two grocery items.
• Calculate the total cost for each item and the grand total.
• Output a summary including the cost of each item and the grand total.
"""

# user input for grocery details 

quantity_OfItem1 = float(input("Enter The Quantity For Item 1:"))
price_OfItem1 = float(input("Enter The Price For Item 1:"))

quantity_OfItem2 = float(input("Enter The Quantity For Item 2:"))
price_OfItem2 = float(input("Enter The Price For Item 2:"))

# spending Limit set 
spending_Limit = float(input("Enter The spending Limit: "))

# calculate Total price of each item 
item1_Total = quantity_OfItem1*price_OfItem1
item2_Total = quantity_OfItem2*price_OfItem2

# Grand total of grocery 
grand_Total = item1_Total+ item2_Total

# printing all the results 
print("\nItem 1 Total: ",item1_Total)
print("Item 2 Total: ",item2_Total)
print("Grand Total: ",grand_Total)
print("Spending Limit : ",spending_Limit)
