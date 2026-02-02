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

