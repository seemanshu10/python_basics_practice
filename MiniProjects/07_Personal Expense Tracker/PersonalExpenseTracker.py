"""
Personal Expense Tracker
Objective:
In this task, you will:
Understand how to organize real-world user data into a structured format.
Learn how to categorize, search, and manage entries within a single data log.
Develop confidence working with persistent data using basic file handling techniques.
Instructions:
Create a terminal-based application to help users track their daily expenses.
Display a welcome message and main menu on every loop.
Keep the program running until the user selects the Exit option.
Store all expenses in a single text file named expenses.txt inside a folder called data (must be created manually in the same directory as the script).
Use with open() for all file operations.
Main Menu Options
Add New Expense
View All Expenses
View Expenses by Category
Exit
Add New Expense
Ask the user to enter:
Date of expense (e.g., 2024-05-01)
Amount (must be a positive number)
Category (e.g., food, travel, utilities)
Description (e.g., lunch, taxi fare)
Save the expense as a single line in expenses.txt using the following format:
2024-05-01 | ₹250 | food | lunch
Append new entries without overwriting existing ones.
Validate that the amount is a number and greater than zero.
Display a confirmation message after a successful entry.
View All Expenses
Read and display all lines from expenses.txt.
Show the data in a clean, tabular format with separators.
If the file is empty or doesn't exist yet, display a message like “No expenses found.”
View Expenses by Category
Ask the user to input a category name (e.g., food).
Display only those entries that match the given category.
If no matching records are found, show a message accordingly.
Display appropriate error messages for:
Invalid input format
Missing or malformed data
File access issues (e.g., file doesn’t exist yet)
"""

EXPENSE_PATH = r"MiniProjects\07_Personal Expense Tracker\data\expenses.txt"

# print table header function 
def tableHeader():
    print("\n" + "-" * 70)
    print(f"{'Date':<15}{'Amount':<15}{'Category':<15}{'Description':<20}")
    print("-" * 70)


# add expense 
def add_NewExpense():
    try:
        date = input("Enter date (YYYY-MM-DD): ").strip()

        # --------------amount validation loop---------

        while True:
            amount_input = input("Enter amount: ").strip()
            try:
                amount = float(amount_input)

                if amount <= 0:
                    print(" Amount must be greater than zero.")         # asking for correct input 
                else:
                    break

            except ValueError:
                print(" Invalid amount. Only numbers are allowed.")

        category = input("Enter category: ").strip().lower()
        description = input("Enter description: ").strip()

        entry = f"{date} | ₹{amount:.2f} | {category} | {description}\n"
        
        with open(EXPENSE_PATH, "a", encoding="utf-8") as file:
            file.write(entry)

        print("Expense added successfully!")

    except KeyboardInterrupt:   # keyboardinterrupt error 
        print("Exiting Cleanly!")
    except FileNotFoundError:
        print("Error Reading the file.")
    

# view All expense 
def view_AllExpense():
    try:
        with open(EXPENSE_PATH, "r", encoding="utf-8") as file:
            expense_data = file.readlines()

        # print(expense_data)
        if not expense_data:
            print("No expenses found.")
            return
        
        tableHeader()

        for expense in expense_data:
            parts = expense.strip().split(" | ")

            if len(parts) != 4:
                print(" Skipping malformed entry.")
                continue

            date, amount, category, description = parts
            print(f"{date:<15}{amount:<15}{category:<15}{description:<20}")

        print("-" * 70)

    except FileNotFoundError:
        print("File Not Found in the file Path.")


# view data by category 
def view_byCategory():

    try:        
        search_category = input("Enter category to search: ").strip().lower()
        with open(EXPENSE_PATH, "r",  encoding="utf-8") as file:
            expense_data = file.readlines()

        if not expense_data:
            print("No expenses found.")
            return
        
        found_category = False
        
        tableHeader()

        for line in expense_data:
            parts = line.strip().split(" | ")

            if len(parts) != 4:
                continue

            date, amount, category, description = parts

            if category.lower() == search_category:
                print(f"{date:<15}{amount:<15}{category:<15}{description:<20}")
                found_category = True

        if not found_category:
            print("No matching records found.")

    except FileNotFoundError:
        print("File Not Found in the file Path.")

# main menu function
def personalMainMenu():
    title = "Welcome to Personal Expense Tracker"
    print("="*70)
    print(title.center(70))
    print("="*70)
    print()

    print("="*70)

    print("Please select an option:")
    print("\n1. Add New Expense")
    print("2. View All Expenses")
    print("3. View Expenses by Category")
    print("4. Exit")
    print("=" * 70)

# display choices and main menu of personalTracker 
def PersonalExpenseTracker():
    try:
        while True:
            personalMainMenu()                                                              # main menu call
            choice = input("\nEnter Your choice! (1-4): ")                                  # choosing the user choice

            if choice == "1":
                add_NewExpense()                                                            # Creating new Expense 
            elif choice == "2":
                view_AllExpense()                                                           # view all Expense function
            elif choice == "3":
                view_byCategory()                                                           # seacrching by category                                            
            elif choice == "4":
                print("Thank you for using the Personal tracker system. Goodbye!")          # exiting 
                break
            else:
                print("Error:Invalid Menu Choice. Please enter between (1-4).")

    except KeyboardInterrupt:                                                               # keyBoardInterrupt error handle
        print("\n\nExiting the Personal tracker system. Exiting Cleanly. Gooodbye!")

PersonalExpenseTracker()