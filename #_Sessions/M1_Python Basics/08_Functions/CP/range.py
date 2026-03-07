"""
Docstring for Functions.CP.range
"""

# Sum of First n Numbers

total_sum =0

for num in range(10):
    total_sum+=num

print("Sum of numbers from 0 to 9:", total_sum)

# Sum of numbers from 0 to 9: 45

# Iterating Over a List with Index

fruits = ["asa","ddfas","dsff"]
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

"""
Index 0: asa
Index 1: ddfas
Index 2: dsff
"""
# Finding Even Numbers
for i in range (10):
        if i%2==0:
            print (i)
"""
0
2
4
6
8
"""

# Filling a List with Values from a Range

squares = []
for i in range(1,6):
     squares.append(i**2)
print("Squares of numbers :",squares)
# Squares of numbers : [1, 4, 9, 16, 25]

# Simple Multiplication Table
for i in range(1,11):
     print(f"3 x {i} = {3*i}")

"""

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
"""

# Generating Fibonacci Sequence

fib = [0,1]
n =10 
for i in range (2,n):
     next_fib = fib[-1] + fib[-2]
     fib.append(next_fib)

print(fib)

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Printing a Sequence of Numbers

for num in range (0,21 , 5):
     print (num)
"""
0
5
10
15
20
"""

# Iteration with a Negative Step

for i in range(10,0,-1):
     print(i) 

"""
10
9
8
7
6
5
4
3
2
1
"""

# Printing Odd Number

for num  in range(1,20,2):
     print (num)

"""
1
3
5
7
9
11
13
15
17
19
"""

# Generating a Reverse Sequence of Cubes

for num in range (5,0,-1):
     print(f"{num}^3 - {num**3}")

"""
5^3 - 125
4^3 - 64
3^3 - 27
2^3 - 8
1^3 - 1
"""