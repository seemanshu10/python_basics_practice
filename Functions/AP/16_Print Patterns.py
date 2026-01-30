"""
Write a Python program to print a right-angled triangle pattern using nested loops. The pattern should look like this:
*
**
***
****
*****
"""

user_input = int(input("Enter The number of rows :"))
for i in range (1,user_input+1):
    for j in range(i):
        print("*",end="") # end  prevents aline break 
    print()

"""
Enter The number of rows :5
*
**
***
****
*****
"""
        
