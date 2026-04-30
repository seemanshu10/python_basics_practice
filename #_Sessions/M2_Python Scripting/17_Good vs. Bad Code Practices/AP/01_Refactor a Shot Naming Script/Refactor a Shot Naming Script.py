# Refactor Script


def main():
    s = input("Enter sequence: ")
    n = input("Enter shot: ")
    v = input("Enter version: ")
    
    if s and n and v:
        print(s + "_" + n + "_" + v)
    else:
        print("Invalid input")

main()
