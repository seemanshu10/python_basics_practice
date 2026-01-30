"""
Python program that prints all odd numbers between 1 and 50 using a for loop and if-else statements.

"""


def odd_numbers():

    # take numbers oone by one till 50 
    for i in range (1,51):
        if i%2==0:
            continue
        else:
            print(i)


# calling Function 
odd_numbers()

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
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
"""
