# ----------- Without else 
# try:
#     pin = int(input("Enter PIN: "))
#     if pin == 1234:
#         print("Withdraw money")
# except ValueError:
#     print("Invalid PIN format")







# --------- with else
try:
    pin = int(input("Enter PIN: "))
except ValueError:
    print("Invalid PIN format")
else:
    if pin == 1234:
        print("Withdraw money")
    else:
        print("Wrong PIN")




















# try:
#     x = 10 / 2 
#     print(x)
    
# except ZeroDivisionError:
#     print("Division by zero")
# else:
#     print("No error occurred") 

# # No error occurred