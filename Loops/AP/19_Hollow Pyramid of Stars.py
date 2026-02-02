"""
Hollow Pyramid of Stars 

### Task Objective

In this task, you will:
* Construct a centered pyramid pattern using nested loops.
* Apply conditional logic to print stars at specific positions.
* Strengthen your understanding of nested iterations with position-based conditions.


### Instructions
* Take an integer input `n` from the user, representing the number of rows.
* Print a centered hollow pyramid using `*` characters.
* Only the left and right edges of each row and the bottom row should have stars.
* All inner positions (not on the edges) should be spaces.

"""

# last Row Stars are 2*n-1 so that is why last row is 9 stars 
n= 5
for i in range(1,n+1):
    for j in range(1,2*n):
        if i == n or j== n-i+1 or j == n+i-1 :
            print("*", end="")
        else:
            print(" ", end="")
    print()


"""
    *    
   * *
  *   *
 *     *
*********
"""