"""

 program that takes a list of integers from the user, removes any duplicate values, and prints the updated list.
"""

# Take Input of a list from user 

list_Num = input("Enter the lsit of integers seperated by spaces : ")

# Covert the input string into a list of integers 
num_list = list(map(int ,list_Num.split()))

print (num_list)
# Enter the lsit of integers seperated by spaces : 12 98 4 3 7 
# [12, 98, 4, 3, 7]

set_num = set(num_list)
final_list = list(set_num)
print ("List without duplicated :  ", final_list)


