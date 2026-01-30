"""
 program to calculate the sum of all even numbers between 1 and 100 using a for loop and if-else statements.
"""
# function to print sum of even num 

def sum_even():
    sum = 0
    # take numbers oone by one till 100
    for i in range (1,101):
        if i%2==0:
            sum+=i
        else:
            continue

    print("Sum of Even numbers between 1 to 100 is: ",sum)

sum_even()

# Sum of Even numbers between 1 to 100 is:  2550