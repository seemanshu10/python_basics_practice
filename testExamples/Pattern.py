
# pattern 

"""
*****
****
***
**
*
"""

#  

# for 5 in range(): 
#     i = i-1
#     for j in range (i):
#         print("*",end="")
#     print()


# col = 8
# for i in range(7): # i :1
#     col= col-1
#     for j in range(col): 
#         #print("*",end="")
#         print("*", end="")
#         #print("#",end="")
#     print()



col = 8
for i in range(7): # i :1
    #col= col-1
    for j in range(col,0,-1): 
        print("*", end="")
    col= col-1
    print()

for i in range(5): 
    for j in range(0,i+1,1):  
        print("*", end="") # end  prevents aline break 
    print()

"""
*
**
* *
*  *
*****

i == n , j==0
"""

print()
n= 5
for i in range(1,n+1):
    for j in range(1,i+1):
        if i == n or j== 1 or j==i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

"""
*
**
* *
*  *
*****

"""

n= 5
for i in range(1,n+1):
    for j in range(1,i+1):
        if j== 1 or j==i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

"""
Output :
*
**
* *
*  *
*   *
"""

print("_"*40)

n= 5
for i in range(1,n+1):
    for j in range(1,2*n):
        if j== 1 or j==i or j==n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print("_"*40)
"""

*   *
**  *
* * *
*  **
*   *
"""

