# ------------------ Creating Nested List  -------------------

nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# ------------ Accessing Elements in Nested Lists ----------------

# Accessing an Entire Inner List
nested_list = [
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9] 
]

print(nested_list[0])
print(nested_list[1])
print(nested_list[2])


# Accessing Elements of inner list
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(nested_list[0][0])
print(nested_list[1][1])


# ---------------- Modifying Nested Listss ----------------

two_d_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original List:")
print(two_d_list)

# Modify an element
two_d_list[1][1] = 50

print("\nModified List:")
print(two_d_list) 