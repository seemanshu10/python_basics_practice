"""
# Description of the Task
Write a Python program that prints all prime numbers between 1 and 100. 
A prime number is a number that is only divisible by 1 and itself.

# Instructions
Use a for loop to iterate through numbers from 1 to 100.
For each number, use another loop to check if it has any divisors other than 1 and itself.
Print the number if it is prime.

# Learning Objective
The objective of this task is to practice:
Using nested loops
Implementing conditional logic with if-else statements
Understanding and applying the concept of prime numbers

# Sample Usage
Example Usage and Expected Output:

Prime numbers between 1 and 100 are:
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
"""


def prime():

    """
    print Prime Numbers  b\w 1 to 100
    
    """
    # loop for numbers  skipped 1 as 1 is not prime  as it has only one factor 
    # outer loop for numbers 
    for num  in range(2,101):
        # loop for divisors 
        is_prime =True
        # inner Loop for check 
        for i in range(2,num):
            if num%i==0 :
                is_prime=False
                break

        if is_prime:
            print(num)

prime()

"""
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
"""

