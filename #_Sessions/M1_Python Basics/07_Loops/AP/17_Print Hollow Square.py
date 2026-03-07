'''
## 🎯 AP. Print a Hollow Square

### Task Objective

In this task, you will:
* Practice using **nested loops** to control both row and column output.
* Strengthen your understanding of how to place characters based on position logic.
* Build a hollow square pattern by printing characters at border positions only.


### Instructions
* Take an integer input `n` from the user, representing the size of the square (e.g., `n = 5`).
* Print a hollow square using the `*` character:
  * All four borders of the square should be filled with `*`.
  * The inner part of the square should remain empty (spaces only).
* Use nested loops to control rows and columns.
* The square must have `n` rows and `n` columns.


### Sample Output (for n = 5)
*****
*   *
*   *
*   *
*****

'''

"""
Print a Hollow Square

### Task Objective

In this task, you will:
* Practice using **nested loops** to control both row and column output.
* Strengthen your understanding of how to place characters based on position logic.
* Build a hollow square pattern by printing characters at border positions only.

*****     *****
*   *       * *   
*   *       * *  # row -  i , Col = j
*   *       * *
*****     *****
"""

n= 5
for i in range(n):
    for j in range(n):
        if i ==0 or i == n-1 or j== 2 or j == n-1 :
            print("*", end="")
        else:
            print(" ", end="")
    print()


