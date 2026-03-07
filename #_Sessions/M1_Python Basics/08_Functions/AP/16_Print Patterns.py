"""
# Description of the Task
Write a Python program to print a right-angled triangle pattern using nested loops. The pattern should look like this:
*
**
***
****
*****

# Instructions
Use nested loops to print the pattern.
The outer loop should iterate over the number of rows.
The inner loop should print the stars (*) for each row.
Each row should have one more star than the previous row.

# Learning Objective
This task helps beginners understand how to use nested loops to generate patterns. It also reinforces the concept of controlling the number of iterations of a loop based on another loop.

# Sample Usage
Example usage and expected output:
If the program is set to print 5 rows, the output should be:
*
**
***
****
*****
"""

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