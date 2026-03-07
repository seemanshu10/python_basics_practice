# ------------- break statement -----------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# with for loop
for num in numbers:
    if num == 5:
        print(f"Number {num} found! Exiting the loop.")
        break
    print(f"Checked number: {num}")


# with while loop
number = 1

while number < 50:
    if number % 7 == 0:
        print("The first multiple of 7 less than 50 is:", number)
        break
    number += 1


# --------------- continue - Statement ----------------------
numbers = [1, 2, 3, 4, 5]

# with for loop
for num in numbers:
    if num % 2 == 0: 
        continue
    print(num)

# with while loop
number = 1

while number <= 10:
    if number % 2 == 0:
        number += 1
        continue
    print("Odd number:", number)
    number += 1


# ---------------- pass - Statement ----------------------------
numbers = [1, 2, 3, 4, 5]

# with for loop
for num in numbers:
    if num % 2 == 0:
        pass  
    else:
        print(f"Odd number: {num}")


# with while loop
count = 5

while count > 0:
    if count == 3:
        pass
    else:
        print(count)
    count -= 1


