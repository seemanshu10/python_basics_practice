
# handling Empty string 

empty = ""*5
print (empty)
# output nothing empty 

text = "world" * 0
print (text)

text = "Hello" *-3
print (text)

# all of this prints empty line 

# but positive gives ouput 
text = "Hello" *3
print (text) # output: HelloHelloHello 

# repeating char in a string 
char = "* "
pattern = (char)*5
print(pattern) # ouput * * * * *

# multiplying strings with varibles 

word = "Go"
times = 4 
cheer = (word + " ")*times 
print (cheer)
# output : Go Go Go Go 


