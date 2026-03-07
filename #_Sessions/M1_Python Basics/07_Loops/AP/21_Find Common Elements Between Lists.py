'''
## 🎯 AP. Finding Common Elements Between Two Lists 

### Task Objective

In this task, you will:
* Practice nested loop logic to compare elements between two lists.
* Strengthen your understanding of iteration and conditional checking.
* Build logic for detecting and storing common elements without using set operations.


### Instructions

* You are given two predefined lists:
    list1 = [3, 7, 9, 12, 15, 18]
    list2 = [4, 7, 12, 18, 21, 25]
* Your task is to:
  * Use **nested loops** to compare each element in `list1` with each element in `list2`.
  * Find and store the **common elements** that exist in both lists.
  * Avoid adding duplicates in the result.
* Do **not** use `set()` or any other built-in function.


### Sample Output
```
Common elements: [7, 12, 18]
```
'''


# Given Two predefined Strings 

list1 = [3, 7, 9, 12, 15, 18]
list2 = [4, 7, 12, 18, 21, 25]

# list to store common elemnets
common_elements = []

#nested loops to compare elements 
for item1 in list1:
    for item2 in list2:
        if item1 == item2 and item1 not in common_elements:
            common_elements.append(item1)
          
# print the result 
print("Common_elements: ", common_elements)

# Common_elements:  [7, 12, 18]