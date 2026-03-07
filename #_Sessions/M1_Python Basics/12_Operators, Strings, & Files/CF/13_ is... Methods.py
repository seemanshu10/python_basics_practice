# ---------------- isalpha() ----------------
word1 = "Python"
word2 = "Py123"

# print(word1.isalpha())  # True → all letters
# print(word2.isalpha())  # False → contains digits



# # ---------------- isdigit() ----------------
# num1 = "12345"
# num2 = "123abc"

# print(num1.isdigit())  # True → only numbers
# print(num2.isdigit())  # False → contains letters



# ---------------- isalnum() ----------------
mix1 = "#$    "
mix2 = "   "


# print(mix1.isalnum())  # True → letters and numbers
# print(mix2.isalnum())  # False → only spaces



# # ---------------- isspace() ----------------
space1 = "   "
space2 = " "

# print(space1.isspace())  # True → only spaces
# print(space2.isspace())  # False → contains letters



# # ---------------- isupper() ----------------
upper1 = "HELLO"
upper2 = "Hello"

# print(upper1.isupper())  # True → all caps
# print(upper2.isupper())  # False → has lowercase letters



# # ---------------- islower() ----------------
lower1 = "hello"
lower2 = "Hello"

# print(lower1.islower())  # True → all small letters
# print(lower2.islower())  # False → first letter is capital



# # ---------------- istitle() ----------------
title1 = "Hello world"
title2 = "Python"
title3 = "hello"

print(title1.istitle())  # True → "Hello World"
print(title2.istitle())  # True → "Python"
print(title3.istitle())  # False → "hello"
