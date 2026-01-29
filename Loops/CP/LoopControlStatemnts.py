"""
Docstring for Loops.CP.LoopControlStatemnts
"""
# finding the first neagtive number 
numbers = [3,7,8,-2,25,-45]

for num in numbers:
    if num<0:
        print("First negative number is : ",num)
        break

# output : 
# First negative number is :  -2

# First Item with a Value Greater Than 50 in a Dict

scores ={
    'John':45,
    'David':36,
    'Jack':87,
    'Mack':12,
}

for name, score in scores.items():
    if score > 50:
        print("The first score greater than 50 is by:",name)
        break
# The first score greater than 50 is by: Jack

# Finding the First Multiple of 7

numbers = 1

while numbers < 50:
    if numbers%7==0:
        print("First first multiple of 7 less than 50 is : ",numbers)
        break
    numbers+=1

# First first multiple of 7 less than 50 is :  7

# Simulating a Simple Login System

correct_password ='secure123'
attempt =0

while True:
    user_password = input("Enter Your Password:")
    attempt+=1
    if user_password == correct_password:
        print("Login Successfull")
        break
    elif attempt >=3:
        print("Too many attempts. Access denied ")
        break
    else:
        print ("Incorrect Password. Please Try Again.")

"""
Enter Your Password:stgffgd
Incorrect Password. Please Try Again.
Enter Your Password:fgd
Incorrect Password. Please Try Again.
Enter Your Password:gdhy
Too many attempts. Access denied 

Enter Your Password:secure123
Login Successfull

"""

# Continue Statement 

# Skipping Zero in a List of Numbers

numbers = [3,1,0,2,25,0,12]

for num in numbers:
    if num==0:
        continue
    print("Non zero number is : ",num)

"""
Non zero number is :  3
Non zero number is :  1
Non zero number is :  2
Non zero number is :  25
Non zero number is :  12
"""

# Skipping Negative Numbers and Zero

count =-5

while count <=5:
    if count <= 0:
        count+=1
        continue
    print("Positive Number is :" ,count)
    count+=1

"""
Positive Number is : 1
Positive Number is : 2
Positive Number is : 3
Positive Number is : 4
Positive Number is : 5
"""

# Counting Vowel Occurrences in Dictionary Values

data ={
    'first':'Apple',
    'second':'Grapes',
    'third':'Banana',
    'fourth':'cherry',
}

vowel_counts = {
    'a':0,
    'e':0,
    'i':0,
    'o':0,
    'u':0
}

for value in data.values():
    index = 0
    while index <len(value):
        char = value[index]
        if char in vowel_counts:
            vowel_counts[char]+=1
        index+=1
print ("Vowel Counts:",vowel_counts)

# Vowel Counts: {'a': 4, 'e': 3, 'i': 0, 'o': 0, 'u': 0}

# using PAss 

number = [1,2,8,1,58,56]

for num in number:
    if num%2==0:
        pass
    else:
        print(num)
"""
1
1
"""

# Processing User Input Until a Valid Response is Given

valid_password =['secure123','password345','admin23']
user_input =''

while user_input not in valid_password:
    user_input = input("Enter Your Password:")
    pass

print("Valid Password Entered. ")
"""
Enter Your Password:secure123
Valid Password Entered. 
"""

# Implementing Role-Based Access Control

user_roles ={
    'Alice':'admin',
    'Bob':'editor',
    'Jack':'viewer'
}

for user,role in user_roles.items():
    if role == 'admin':
        pass
    elif role == 'editor':
        pass
    elif role == 'viewer':
        pass
print("User Roles Have Been Checked (implementation coming soon).")

# User Roles Have Been Checked (implementation coming soon).