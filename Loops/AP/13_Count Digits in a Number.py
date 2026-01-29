"""
 program that takes a number as input from the user and counts the number of digits in the number using a while loop.
"""

# input number 

num = int(input("Input A Number: "))

# store The reversed num 
count = 0

# reverse the num using while 
while num >0:
    #digit = num%10 # getting the last digit 
    count +=1  # increase count 
    num = num//10 # remove the last digit 

# Print The Count 
print ("Total Number of Digits:",count)

"""
Input A Number: 2354
Total Number of Digits: 4
"""