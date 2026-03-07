# ------------------ Common Mistakes in Exception Handling ------------------------

# Catching All Exceptions Too Broadly
try:
    # for i in range(name):
    #     print(i)

    num1 = 10
    num2 = 0 
    result = num1 / num2

    # my_list = [1, 2, 3]
    # print(my_list[5]) 

    # with open("non_existent_file.txt", 'r') as file:
    #     content = file.read()   

except ZeroDivisionError:
    print("Division by Zero Not possible")
except FileNotFoundError:
    print("File not Exist")
except IndexError:
    print("Index out of range")
except Exception as e:
    print(e)


# Ignoring the Exception
# try:
#     value = int(input("Enter a number: "))
# except ValueError:
#    print("Hello")


# n = "hello"

# print(n[8])


# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# result = num1 / num2
# print(f"Result: {result}")

# with open("non_existent_file.txt", 'r') as file:
#     content = file.read()   
