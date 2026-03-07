#---------------- Using 'is' ---------------------------
a = [10, 20, 30]
b = a       # b references the same object as a
c = [10, 20, 30]

print(a is b)   # True (same object)
print(a is c)   # False (different objects with same content)



#---------------- Using 'is not' -----------------------
x = "Python"
y = "Python"
z = "Java"

print(x is not y)  # False (same object in memory due to string interning)
print(x is not z)  # True (different objects)



#---------------- Identity with numbers ----------------
num1 = 256
num2 = 256
num3 = 300
num4 = 300

print(num1 is num2)  # True (small integers cached by Python)
print(num3 is num4)  # False (larger integers stored separately)



#---------------- Identity with mutable objects ----------
list1 = [10, 20]
list2 = list1
list3 = list1.copy()

print(list1 is list2)   # True (same object reference)
print(list1 is list3)   # False (copy creates a new object)



#---------------- Identity with None ---------------------
value = None

if value is None:
    print("Value is None")   # This will print