"""
Docstring for Lists.ListFunction
create a list and do all available operations on it . 

"""

# taking input in an empty list  

num_List = []
num = int(input("Enter The number to Add on list : "))

num_List.append(num)

print (num_List)
num_List.pop()
    
#num_List.append(12)
#print(num_List)
    
num_List.insert(0,5)
#print (num_List)
    
num_List.insert(1,10)
#print (num_List)
    
num_List.insert(0,6)
print (num_List)
    
num_List.remove(6)
    

num_List.append(9)
num_List.append(1)
print (num_List)

num_List.sort()
print (num_List)
num_List.pop()
print
num_List.reverse()


