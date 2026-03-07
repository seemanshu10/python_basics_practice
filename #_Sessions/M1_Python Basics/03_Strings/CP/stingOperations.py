# check if a substring exist within string 
# or if the substring is not in the string 
text = "hello World"
print ("world" in text) # output : False 

text = "hello world" # they are case sensitive 
print ("world" in text) # output : False 

# special Characters 

text = "hello#world!"
print ("*"not in text) # True
print ("#" in text)  # True
print ("#" not in text) # False

# substring not found 

text = "hello World "
result = "Python" not in text

print (result) # true


