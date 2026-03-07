"""
Iterating through string 
"""
# count characters in string 
sen = "Hello World"
count = 0

for char in sen:
    count+=1 # increment 
print ("Total Number Of characters:",count)
# Total Number Of characters: 11

# Counting Specific Characters 

sen = "Hello World"
target_char = 'o'
count = 0
for char in sen:
    if char == target_char:
        count+=1 # increment 
print (f"Total Number Of '{target_char}'characters:",count)

# Total Number Of 'o'characters: 2

# Extracting Vowels From A string 

sen = "Hello World"
vowels  = ""

for char in sen:
    if char in 'aeiouAEIOU':
        vowels+=char # increment 
print(f"Vowels in string:",vowels)
# Vowels in string: eoo

# summing Elelments in list 

num = [10,20,30,40]
total_sum = 0

for n in num:
    total_sum+=n
print("Sum of all:",total_sum)
# Sum of all: 100

# Filtering Even numbers from a list 

num = [1,2,3,4,5,6,7,8,9,10]
even = []

for n in num:
    if n%2==0:
        even.append(n)

print("Even Numbers:",even)
# Even Numbers: [2, 4, 6, 8, 10]