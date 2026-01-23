"""
Indexing in lists 
"""
# creating a list 
# indexing with numbers 
number = [10,20,30,40,50]

print(number[0])  # output: 10
print(number[3])  #output: 40
print(number[2])  # output: 30
print(number[4])  # output: 50

# accessing the last element 

city = ["New york","Delhi","Mumbai","Washington","Sydney"]

print(city[3]) # output: Washington

# indexing with mixed Data types 

mix = ["New york",2,"India",3.14,True]
print(mix[3]) # output: 3.14

# accesing element in a list of decimal numbers  
numbers = [10.4,4.5,6.5,1.2]
print (numbers[2])  # output: 6.5
 
# lsit length with positive indexing 

planets = ["Mercury","Venus","Earth","Mars"]
print (planets[len(planets)-2]) 

# output: Earth

# accesing elemnts through negative values 

numbers = [10.4,4.5,6.5,1.2]
print(numbers[-3])

# output: 4.5
