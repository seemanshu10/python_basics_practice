# empty strings 

text = ""
length = len(text)
print (length)

# output :0

# string with spaces 

text = "__name__"
length = len(text)
print(length)

# output : 8

# length of numeric characters 

# numbers is a string counted as char 

text = "123456"
length = len(text)
print(length)
# output : 6

# UPPER 
# string With Spaces 
text = "hello       World   "
print(text.upper())
# output : HELLO       WORLD

# multiple words 
text = "good morning everyone "

upperCase = text.upper()
print(upperCase)
# output 'GOOD MORNING EVERYONE'

# already uppercase 

text = "HELLO WORLD"
upper = text.upper()
print (upper)

# lowerCase 
text = "HELLO       World   "
print(text.lower())
# output : Hello       World

# multiple words 
text = "GOOD MORNING EVERYONE "

upperCase = text.lower()
print(upperCase)
# output 'good morning everyone'

# already uppercase 

text = "HELLO WORLD"
upper = text.lower()
print (upper)


# strip - remmoves whitespoaxes  

text = "trailing spaces      "
strip_text = text.strip()

print(strip_text) # output : trailing spaces

# strip with newkines and Tabs 

text = "\n\t hello World  \t\n"
strip_text = text.strip()

print(strip_text) # hello World

# replace 

# replace with empty String 

text = "remove spaces "
replace_text = text.replace("spaces","")
print(replace_text) 
# output : remove 

# replace non - existing Substring 

text = "hello world"
print (text.replace("world","Python"))
# output : hello Python

# replace with special characters 

text = "hello @world@"
print (text.replace("@","#"))
# output hello #world#

# split Method 
# basic Split 

text = "hello Python is great "
print(text.split())
# output : ['hello', 'Python', 'is', 'great']

#  split wirh Custom Delimiter 

data = "apple , oranges , grapes"
print (data.split(','))

# output : ['apple ', ' oranges ', ' grapes']

# handling Multiple Conseccutive Delimiter

text = 'a,,b,,c'
split_text= text.split(",")
print (split_text)

#output : ['a', '', 'b', '', 'c']
# find to find gives first index  of occurance 
# multiple occurances 
data = "apple , oranges , grapes"
print (data.find("oranges"))

# output : 8 

text = ""
index= text.find("text")
print (index) # output : -1

# count - gives the numbver of elememts 

text = "Hellp Hello "
print (text.count("Hello"))


# startsWith () - gives true false if condition true or not 

text = "hello World "
start = text.startswith("hello")
print(start)
# Output : True

# prefix not  present

text = "hello World"
start =  text.startswith("World")
print (start) 
# Output : False 

# with all the arguments 

text = "Learning python is fun"
start =  text.startswith("python",9,15)
print (start) 

# Output : True

text = ""
start =  text.startswith("")
print (start) 

# Output : True

text = "Hello World !"
start =  text.startswith("world",7)
print (start) 

# Output : False

# case Sensitive 
text = 'Hello World'
start = text.startswith("hello")

print(start)
# Output : False

# ends With 

text = "Python Programming"
end =  text.endswith("Python",0,6)
print (end) 

# Output : True

text = "Learning Python is fun!"
end =  text.endswith("python",0,15)
print (end) 

# Output : False

# using len() function 

text = "Python programming is Powerful"
print(text.endswith("Powerful",0,len(text)))

# outut : True 
