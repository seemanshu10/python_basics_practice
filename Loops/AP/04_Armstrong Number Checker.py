"""
checks whether a number entered by the user is an Armstrong number. 
An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
"""

# Prompt the user to enter a number
num = int(input("Enter a number: "))

# Convert the number to a string to easily get digits
num_str = str(num)

# Calculate the number of digits
num_digits = len(num_str)

# Compute the sum of each digit raised to the power of the number of digits
sum_of_powers = 0
for digit in num_str:
    sum_of_powers += int(digit) ** num_digits

# Check if the computed sum is equal to the original number if yes then armstrong otherwise not 
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

"""
Enter a number: 123
123 is not an Armstrong number.

Enter a number: 524
524 is not an Armstrong number.
"""




