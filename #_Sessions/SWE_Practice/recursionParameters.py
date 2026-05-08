
def print_number(x, n):
    if n == 0:
        return

    print(x)
    print_number(x, n-1)

print_number(2, 5)