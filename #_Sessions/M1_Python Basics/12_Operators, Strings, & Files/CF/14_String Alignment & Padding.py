#---------------- Left-align ljust(width, ch) ----------------
text = "Python"

# print(text.ljust(4, '-'))   # Output: Python----



#---------------- Right-align rjust(width, ch) ---------------
print(text.rjust(10, '*'))   # Output: ****Python



# #---------------- Center-align center(width, ch) ------------
print(text.center(12, '.'))  # Output: ...Python...



# #---------------- Pad with zeros zfill(width) ----------------
number = "2"

print(number.zfill(2))       # Output: 00042