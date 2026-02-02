"""
Finding the Second Largest Number

### Task Objective
In this task, you will:
* Practice loop-based logic to identify the second largest value in a list.
* Learn how to track and update multiple comparison variables.
* Avoid using shortcuts or built-in functions to strengthen raw logic skills.

### Instructions
* You are given a predefined list of numbers:
  numbers = [12, 45, 23, 67, 34, 89, 67, 21]
* Your task is to:
  * Use a loop to find the **largest** number.
  * Use logic to find the **second largest** number without using `sort()` or `max()`.
* If the largest number appears more than once, still treat it as a single largest value.
* Do **not** sort the list or use built-in shortcuts.
>  Do not use built-in sorting or max functions.

"""
# predefined list of numbers 
numbers = [12, 45, 23, 67, 34, 89, 67, 21]

# define largest , second largest variable 

largest = 0
second_largest = 0

# iterate through list 
for num in numbers:
    if num > largest:
        second_largest = largest # previous largest becomes second largest 
        largest = num  # update largest 
        
    elif num > second_largest and num != largest:
        second_largest = num    # update second largest if num is smaller than largest 

# Sceond Largest is saving first 67 if the 
print("Largest number is :", largest)
print("Second Largest number is :", second_largest)

"""
Largest number is : 89
Second Largest number is : 67
"""

