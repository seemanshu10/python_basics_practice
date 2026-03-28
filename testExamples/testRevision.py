
# list_num = input("Enter the list of integers seperated by spaces: ")
# # this takes input but is still as string 

# # print(list_num)
# # print(type(list_num))
# # 78 15 6 9 7
# # <class 'str'>

# # split from spaces add 
# split_from_spaces= list_num.split()
# # print(type(split_from_spaces))
# # ['23', '1', '85', '4', '3'] 
# # <class 'list'>

# list_numbers_int = []
# for i in split_from_spaces:
#     int_num = int(i)
#     list_numbers_int.append(int_num)

# print(list_numbers_int)

# asc_sort = sorted(list_numbers_int)
# print(asc_sort)
# # [1, 2, 3, 4, 64]

# list_num = list(map(int, list_num.split()))
# print(list_num)

# max_num = max(list_num)
# print(max_num)

# print(min(list_num))

# rever_list = list_num[::-1]
# print(rever_list)


# two_d_list = [
#     [1,4,22],
#     [8,1,8],
#     [10,6,2]
# ]

# print("Original List: ")
# print(two_d_list)

# # modify an elemnet 
# two_d_list[1][1] = 50

# print("\nModified list:")
# print(two_d_list)

# dictionary lookup 

my_dict = {
    'apple':' A sweet red fruit',
    'banana':'A long yellow fruit',
    'grapes':'A sweet Green fruit'
}

user_input = str(input("Enter a key to search:"))
if user_input in my_dict:
    print("Value : ", my_dict[user_input])

else:
    print("Eror, key not found")