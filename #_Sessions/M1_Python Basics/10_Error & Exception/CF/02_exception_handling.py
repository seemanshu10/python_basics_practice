# try and except block
# try:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     result = num1 / num2
#     print(f"Result: {result}")
# except ZeroDivisionError:
#     print("undefined")



















# # Multiple except block
# try:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     result = num1 / num2
#     print(f"Result: {result}")
#     with open("demo.txt", "r") as file :
#         f = file.read()
#         print(f)

# except ValueError:
#     print("Error: Invalid input, please enter numbers!")
# except FileNotFoundError:
#     print("hello")


# # Catching All Exceptions
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"Result: {result}")
    with open("demo.txt", "r") as file :
        f = file.read()
        print(f)
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
except:
    print("An error occurred.")