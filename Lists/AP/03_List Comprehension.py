"""
create a list of the first 20 natural numbers and generate a 
new list containing the squares of these numbers using list comprehension.

"""

list_Num = input("Enter the list of integers seperated by spaces : ")

num_list = list(map(int ,list_Num.split()))
squared_list = [] 
for num in num_list: 
    squared = num **2
    squared_list.append(squared)
print (squared_list)