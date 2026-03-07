# ----------------- is and in Keywords ----------------

# using is
a = 1000
b = 1000

if a is b:
    print("Both 'a' and 'b' are the same object in memory.")
else:
    print("They are different objects in memory.")


# Using 'in'
my_string = "Hello, World!"

if "World" in my_string:
    print("'World' is in the string.")
else:
    print("'World' is not in the string.")

# ------------------ Using “is not” and “not in” ----------------

a = 1000
b = 1000

# using is not
if a is not b:
    print("The variables 'a' and 'b' do not refer to the same object in memory.")
else:
    print("The variables 'a' and 'b' refer to the same object in memory.")


# using not in
text = "Hello, World!"

if "Python" not in text:
    print("The substring 'Python' is not found in the text.")
else:
    print("The substring 'Python' is found in the text.")