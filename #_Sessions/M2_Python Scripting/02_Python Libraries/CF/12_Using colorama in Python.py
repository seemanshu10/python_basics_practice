# ------------------ Changing Text Colors --------------------
from colorama import Fore, Style

# print(Fore.GREEN + "Hello World")
# print(Style.RESET_ALL)






# ---------------- Adding Color to Terminal Text ---------------
from colorama import Fore, Back, Style

# Red text
print(Fore.RED + 'This is red text')
print(Style.RESET_ALL)


# Green background with default text color
print(Back.GREEN + 'This has a green background')
print(Style.RESET_ALL)

# Dim style
print(Style.DIM + 'This is dim text')


# Reset all styles to default
print(Style.RESET_ALL)

# Back to normal text
print('Now we are back to normal.')

