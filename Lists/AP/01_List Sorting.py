"""
Creates a list of integers.
Sorts the list in ascending and descending order.
Prints both sorted lists.
"""
list_Num = input("Enter the list of integers seperated by spaces : ")

num_list = list(map(int ,list_Num.split()))

asc_sort = sorted(num_list)
print ("The Acsending Order :",asc_sort)

dsc_sort = sorted(num_list,reverse=True)
print ("The Decssending Order :",dsc_sort)

"""
Enter the list of integers seperated by spaces : 3 1 88 4 2 6 4 
The Acsending Order : [1, 2, 3, 4, 4, 6, 88]
The Decsending Order : [88, 6, 4, 4, 3, 2, 1]
"""
