"""
Write a Python program to print a right-angled triangle pattern using nested loops. The pattern should look like this:
*
**
***
****
*****
"""

user_input = int(input("Enter the number: "))
for i in range(user_input): 
    i = i+1
    for j in range(i):  
        print("*", end="") # end  prevents aline break 
    print()

"""
Enter The number of rows :5
*
**
***
****
*****
"""
# for i in range(0):
#     print(i)