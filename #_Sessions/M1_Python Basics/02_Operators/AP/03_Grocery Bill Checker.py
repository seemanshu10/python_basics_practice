"""
✅ Task Objective:

• Accept user input for the quantity and unit price of two grocery items.
• Calculate the total cost for each item and the grand total.
• Output a summary including the cost of each item and the grand total.

📝 Instructions:

1. Prompt the user to enter:
   • Quantity and unit price for Item 1
   • Quantity and unit price for Item 2
   • Their total spending limit

2. Perform the following calculations:
   • Item 1 Total = quantity × unit price
   • Item 2 Total = quantity × unit price
   • Grand Total = Item 1 Total + Item 2 Total

3. Display the following:
   • Total cost of Item 1
   • Total cost of Item 2
   • Grand Total
   • Spending Limit (no need to compare it yet)

💡 Sample Output:

Enter quantity for Item 1: 3  
Enter unit price for Item 1: 2.5  
Enter quantity for Item 2: 2  
Enter unit price for Item 2: 5.0  
Enter your spending limit: 20  

Item 1 Total: 7.5  
Item 2 Total: 10.0  
Grand Total: 17.5  
Spending Limit: 20.0
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
