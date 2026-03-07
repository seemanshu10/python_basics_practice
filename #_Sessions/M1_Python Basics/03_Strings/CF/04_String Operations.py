'''
Comparison Operators -  Compare two strings lexicographically 
    - ==   : Equal to
    - !=   : Not equal to
    - <    : Less than
    - >    : Greater than
    - <=   : Less than or equal to
    - >=   : Greater than or equal to
    
 Lexicographical comparison : comparing strings character-by-character using their ASCII values.
'''

# First Characters Are Different
print("banana" < "cherry")  

# # Same Start, Difference Comes Later
print("banana" < "bherry")  


# # Strings Start the Same, But Differ Later
print("file1" < "file2")  


# # One String is a Shorter Version of the Other
print("apple" < "apples")  


# # Comparison is case-sensitive
print("Apple" < "apple")



# All Operators 
str1 = "banana"
str2 = "cherry"

# print(str1 == str2)   # False
# print(str1 != str2)   # True
# print(str1 < str2)    # True
# print(str1 > str2)    # False
# print(str1 <= str2)   # True
# print(str1 >= str2)   # False








'''
 Membership Operators
    in    
    not in 
'''
 
greeting = "Hello, World!"

print('H' in greeting)       
print('z' in greeting)       

print('World' in greeting)    
print('world' in greeting)    

print('Hello' not in greeting) 
print('Python' not in greeting)


