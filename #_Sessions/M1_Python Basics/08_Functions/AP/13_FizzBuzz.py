"""
# Description of the Task
Create a Python program that prints the numbers from 1 to 50. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".

# Instructions
Use a for loop to iterate through numbers from 1 to 50.
For each number, check if it is a multiple of 3 and 5, 3 only, or 5 only.
Print "FizzBuzz" for multiples of both 3 and 5.
Print "Fizz" for multiples of 3.
Print "Buzz" for multiples of 5.
Print the number itself if it is not a multiple of 3 or 5.

# Learning Objective
Understand the use of loops and conditionals in Python.
Practice writing and organizing if-else statements.
Learn how to apply modulo operation to check divisibility.

# Sample Usage
Example Usage and Expected Output:
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
"""

"""
Create a Python program that prints the numbers from 1 to 50. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".
"""

# defining fizzBuzz function
def fizzBuzz():
    for i in range (1,51):  # iterate from 1 to 50 
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(str(i))

# calling Fizzbuz 
fizzBuzz()

"""
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz

"""
