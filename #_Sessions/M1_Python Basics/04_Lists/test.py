# data = "apple , oranges , grapes"
# print (data.split(','))
# print (type(data)) # Class of strings Returns - Output  as a list of strings or substrings 

num = input("Input then numbers with a comma :" )
split_num = num.split(",")

# spliting and giving the substring output is list os string  
print(split_num) 
print(type(split_num)) # type : List of substrings  

# map explitily converts to int of the split strings 
nums =map(int,split_num)
print(type(nums)) # Type : map 

# now here the map output is map so converting to string by typecasting 
list_num = list(nums)
print(list_num) 
print(type(list_num)) # Type : list 

# now to remove duplicates the list is passed or converted to set which cannot hold the duplicate numbers 
set_list = set(list_num)
print(set_list)
print(type(set_list)) # Type : set

# now here the set is converted back to list to print the final output and process foraward 
list_noDup = list(set_list)
print(list_noDup) 
print(type(list_noDup)) # type : list

