# basic positional Arguments 

# using positional argument to format a string 

text = "{0} is {1} years old. ",format("Alice","30")
print(text)

# index reordering 
text = "{1} is the name of the person . {0} is their age.".format("25","david")
print (text)

# nested formatiing 

text = "The Price is {0} is (1:.2f) . With Tax , it become (2:.2f).".format("a book ","12.49",225)

print (text)

