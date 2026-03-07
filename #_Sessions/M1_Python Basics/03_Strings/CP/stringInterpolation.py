# interpolation means inserting values in string 
# using expressions inside fstrings 
a,b=5,10

print (f"The Sum of {a} and {b} is {a+b}")
# output : The Sum of 5 and 10 is 15

# formatting numbers in f-strings 
pi = 3.14159232859
print (f"PI to 3 decimal Places: {pi:.3f}")

# R- strings(Raw Strings)

# basic Raw String 

raw= r"Hello\nWorld"
print(raw)

# output : Hello\nWorld

# raw Strings with File Path 
file = r"D:\PipelineTD\Sessions\Day2\Errors.py"

print (file)