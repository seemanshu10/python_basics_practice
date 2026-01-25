"""
 that performs various operations on a list of numbers. You'll create a list, perform different operations like finding the largest and smallest numbers, calculating the sum of all numbers, and printing the list in reverse order.

"""

list_Num = input("Enter the list of integers seperated by spaces : ")

num_list = list(map(int ,list_Num.split()))

print ("The list Entered is :" , num_list)
# output : The list Entered is : [1, 3, 9, 7, 2, 1]
max_num = max(num_list)
print ("MAX number is : ",max_num)

min_num = min(num_list)
print ("MIN number is : ",min_num)

sum_total = sum(num_list)
print ("SUM of list is : ",sum_total)
# output : The list Entered is : [3, 2, 122, 4, 6, 3, 1]
# MAX number is :  122
# MIN number is :  1
# SUM of list is :  141

rever_list = num_list[::-1]
print("Reversed list is :", rever_list)

# Reversed list is : [1, 3, 6, 4, 122, 2, 3]