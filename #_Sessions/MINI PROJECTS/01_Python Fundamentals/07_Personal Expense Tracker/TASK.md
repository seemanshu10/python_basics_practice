## **PA. Personal Expense Tracker**

### **Objective:**
* In this task, you will:
  * Understand how to organize real-world user data into a structured format.
  * Learn how to categorize, search, and manage entries within a single data log.
  * Develop confidence working with persistent data using basic file handling techniques.

### **Instructions:**
* Create a terminal-based application to help users track their daily expenses.
* Display a welcome message and main menu on every loop.
* Keep the program running until the user selects the Exit option.
* Store all expenses in a single text file named `expenses.txt` inside a folder called `data` (must be created manually in the same directory as the script).
* Use `with open()` for all file operations.
* **Main Menu Options**
  * Add New Expense
  * View All Expenses
  * View Expenses by Category
  * Exit
* **Add New Expense**
  * Ask the user to enter:
    * Date of expense (e.g., `2024-05-01`)
    * Amount (must be a positive number)
    * Category (e.g., food, travel, utilities)
    * Description (e.g., lunch, taxi fare)
  * Save the expense as a single line in `expenses.txt` using the following format:
    ```
    2024-05-01 | ₹250 | food | lunch
    ```
  * Append new entries without overwriting existing ones.
  * Validate that the amount is a number and greater than zero.
  * Display a confirmation message after a successful entry.
* **View All Expenses**
  * Read and display all lines from `expenses.txt`.
  * Show the data in a clean, tabular format with separators.
  * If the file is empty or doesn't exist yet, display a message like “No expenses found.”
* **View Expenses by Category**
  * Ask the user to input a category name (e.g., `food`).
  * Display only those entries that match the given category.
  * If no matching records are found, show a message accordingly.
* Display appropriate error messages for:
  * Invalid input format
  * Missing or malformed data
  * File access issues (e.g., file doesn’t exist yet)

### **Sample Expense File Format (For Reference):**
```
2024-05-01 | ₹250 | food | lunch
2024-05-01 | ₹600 | travel | cab to airport
2024-05-02 | ₹1200 | utilities | electricity bill
```

###  **Sample Output:**
```
========================================
 Welcome to Personal Expense Tracker
========================================

========================================
Please select an option:
1. Add New Expense
2. View All Expenses
3. View Expenses by Category
4. Exit
========================================
Enter your choice (1-4): 1
 Add New Expense ---
Enter date (YYYY-MM-DD): 2024-05-02
Enter amount: 1200
Enter category: utilities
Enter description: electricity bill
✅ Expense added successfully!
```
