"""
Objective:
Build a complete terminal-based banking system using Python fundamentals by applying variables, conditionals, loops, functions, file handling, and user input/output processing.

Instructions:
Create a terminal-based Python application for basic banking operations.
Display a welcome message and menu options every time the program runs.
Keep the program running until the user chooses to exit.
Store all account data in text files inside an accounts folder (must be created manually in the same directory as the script).
Use with open() (context manager) for all file operations.
Do not use external modules such as os, getpass, or any third-party libraries.
Create Account
Ask the user for an account holder name.
Ask the user to set a 4-digit PIN.
Validate that the PIN contains only digits and is exactly 4 characters long.
Create a new text file inside the accounts folder using the account holder name.
Prevent account creation if a file with the same name already exists.
Store the following information inside the account file:
Name
PIN
Balance (initially set to 0)
View Balance
Ask the user for the account name.
Ask the user for the PIN.
Validate the entered PIN against the stored PIN.
Display the account holder name and current balance using formatted output with separators.
Deposit Money
Ask the user for the account name and PIN.
Ask for the amount to deposit.
Ensure the deposit amount is a positive number.
Add the deposited amount to the existing balance.
Update the account file with the new balance.
Display a success message along with the updated balance.
Withdraw Money
Ask the user for the account name and PIN.
Ask for the amount to withdraw.
Ensure the withdrawal amount is a positive number.
Check that the account has sufficient balance before withdrawing.
Deduct the amount from the balance and update the account file.
Display a success message along with the remaining balance.
Display meaningful error messages for:
Invalid menu choices
Incorrect PIN
Invalid amounts
Missing account files

"""
# =========================
# Terminal Banking System
# =========================

ACCOUNTS_PATH = r"MINI PROJECTS\01_Python Fundamentals\03_Banking System\accounts"

# display bank menu options
def bank_menu():
    print("\n" + "=" * 40)
    print("  Welcome to New Bank of India")
    print("=" * 40)
    print("\nPlease select an option:")
    print("1. Create Account")
    print("2. View Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")
    print("=" * 40)

# checking if pin is valid it should be digit and len should be exactly 4
def valid_pin(pin):
    return pin.isdigit() and len(pin) == 4

# build account file path
def account_path(name):
    return rf"{ACCOUNTS_PATH}\{name}.txt"

# checking and loading account details
def load_account(account_name):
    try:
        with open(account_path(account_name), "r") as file:
            lines = file.readlines()                            # reading all content
            # print(lines)
             
            acc_name = lines[0].split(": ")[1].strip()              # reading Account holder name
            acc_pin = lines[1].split(": ")[1].strip()               # reading Account Pin 
            acc_balance = float(lines[2].split(": ")[1].strip())    # reading balance     
            return acc_name, acc_pin, acc_balance
        
    except FileNotFoundError:
        print("Error: Account does not exist.")

# save account details
def save_account(name, pin, balance):
    with open(account_path(name), "w") as file:
        file.write(f"Name: {name}\n")                       # writing Account holder name
        file.write(f"PIN: {pin}\n")                         # writing pin number 
        file.write(f"Balance: {balance}\n")                 # writing Balance number

# View balance
def display_balance():
    while True:
        name = input("Enter Account name: ").strip()
        account = load_account(name)
        if account:
            break

    acc_name, acc_pin, balance = account

    while True:
        pin = input("Enter The PIN: ").strip()
        if pin == acc_pin:
            break
        print("Error: Incorrect PIN. Try Again.")

    print("\n" + "-" * 30)
    print(f"Account Holder: {acc_name}")
    print(f"Current Balance: ${balance:.2f}")
    print("-" * 30)

# creating deposit money function
def credit_account():
    while True:
        name = input("Enter account name: ").strip()
        account = load_account(name)
        if account:
            break

    acc_name, acc_pin, balance = account            # storing the values from account details 

    while True:
        pin = input("Enter PIN: ").strip()
        if pin == acc_pin:
            break
        print("Error: Incorrect PIN. Try again.")

    while True:
        try:
            amount = float(input("Enter deposit amount: ").strip())
            if amount > 0:
                break
            print("Error: Deposit amount must be positive.")
        except ValueError:
            print("Error: Invalid amount.")

    balance += amount                   # Adding the amount to balance
    save_account(acc_name, acc_pin, balance)

    print(f"Deposit successful! New balance: ${balance:.2f}")

# Creating debit money function
def debit_account():
    while True:
        name = input("Enter account name: ").strip()    # Account name 

        # Load ing account details 
        account = load_account(name)
        if account:
            break

    acc_name, acc_pin, balance = account

    while True:
        pin = input("Enter PIN: ").strip()
        if pin == acc_pin:
            break
        print("Error: Incorrect PIN. Try again.")

    while True:
        try:
            amount = float(input("Enter withdrawal amount: ").strip())
            if amount <= 0:
                print("Error: Withdrawal amount must be positive.")
            elif amount > balance:
                print("Error: Insufficient balance.")
            else:
                break
        except ValueError:
            print("Error: Invalid amount.")

    balance -= amount                       # removing the amount from balance
    save_account(acc_name, acc_pin, balance)

    print(f"Withdrawal successful! Remaining balance: ${balance:.2f}")

# create new account
def creating_account():
    while True:
        name = input("Enter Account holder name: ").strip()
        try:
            with open(account_path(name), "r"):
                print("Error: Account already exists.")

        except FileNotFoundError:
            break
    
    while True:
        pin = input("Set a 4-digit PIN: ").strip()
        if valid_pin(pin):
            break
        print("Error: PIN must be exactly 4 digits.")

    # Ask user for initial balance
    while True:
        try:
            balance = float(input("Enter initial deposit amount: ").strip())
            if balance >= 0:
                break
            print("Error: Amount must be zero or positive.")
        except ValueError:
            print("Error: Please enter a valid number.")

    save_account(name, pin, balance)

    print("New Account Created successfully")

# display choices
def Bank_System():
    try:
        while True:
            bank_menu()
            choice = input("Choose an option (1-5): ").strip()

            if choice == "1":
                creating_account()
            elif choice == "2":
                display_balance()
            elif choice == "3":
                credit_account()
            elif choice == "4":
                debit_account()
            elif choice == "5":
                print("Thank you for using the banking system. Goodbye!")
                break
            else:
                print("Error: Invalid menu choice.")
                
    except KeyboardInterrupt:
        print("\n\nKeyboard Interrupt detected. Exiting the banking system. Goodbye!")

Bank_System()
