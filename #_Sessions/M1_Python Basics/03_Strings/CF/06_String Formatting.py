name = "Ravi"
age = 25
city = "Pune"

# print("My name is " + name + ", I am " + str(age) + " years old and I live in " + city)



"'"
\t
\n
\'
\"
\\
'''



print(r"C:\Users\pralhad\Desktop\Cohort-EC1\#_Sessions\M1_Python Basics\03_Strings\CF\07_String Interpolation.py")











# # %s  -- !important
# name = "45"
# age = 45
# height = 5.934

# print("Hello, %s!" % name)


# print("I am %d years old." % age)
# print("I am %.1f feet tall." % height)


# # %c
# initial = "A"
# print("My initial is %c." % initial)



# '''
# {} str.format() Method 
# '''

# name = "Bob"
# age = 30

# # Using {}
# greeting = "Hello, {}! You are {} years old.".format(name, age)
# # print(greeting)

# # Using format specifiers
# # print("Name: {:s}, Age: {:d}".format(name, age))







# '''
# {0} str.format() Positional Arguments
# '''

# # {0}
# name = "Charlie"
# age = 28

# print("Hello, {0}! You are {1} years old.".format(name, 65))



# # print(greeting)


# # Reorder Indexes
# age_statement = "{1} is the age of {0}.".format(name, age)
# # print(age_statement)




# '''
# {name} str.format() Keyword Arguments
# '''
# # Basic Usage
# name = "Diana"
# age = 35

# greeting = "Hello, {name}! You are {age} years old.".format(name=name, age=age)
# # print(greeting)




# # Example 2
# name = "Alice"
# char = "A"
# first_var = "Eve"


# # print("My name is {third_var}, and my char is {second_var}.\nSecond name: {fifth_var}".format(
# #     first_var=name,
# #     second_var=char,
# #     third_var="12",
# #     fourth_var="fourth_var",
# #     fifth_var=first_var
# # ))