# -------basic use

# if age < 0:
#     print("age should not be Negative")

#     # raise ValueError("Age cannot be negative")
    
# print("Age accepted")




# ---------raise with try except
age = -5

try:
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print("Error:", e)
else:
    print("Age accepted")


if age < 0:
    raise ValueError("Age cannot be negative")
