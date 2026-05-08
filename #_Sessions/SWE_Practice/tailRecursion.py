count = 0  
def print_name():
    global count
    if count == 4:
        return
    count += 1
    print_name()
    print(f"I printed {count}")


print_name()