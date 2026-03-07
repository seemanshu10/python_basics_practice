# ----------- Without Finally

# try:
#     num = int(input("Enter number: "))
#     result = 10 / num
#     print("Result:", result)
# except ValueError:
#     print("Invalid input")

# print("Program finished")







# --------------- with finally

try:
    num = int(input("Enter number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("Invalid input")
finally:
    print("Program finished")











# ------------- Combine Finally & else
try:
    num = int(input("Enter number: "))
    result = 10 / num
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Number cannot be zero")
else:
    print("Result:", result)
finally:
    print("Program finished")
