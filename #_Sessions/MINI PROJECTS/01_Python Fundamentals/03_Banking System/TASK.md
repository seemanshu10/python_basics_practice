## **PA. Banking System**

### **Objective:**
Build a complete terminal-based banking system using Python fundamentals by applying variables, conditionals, loops, functions, file handling, and user input/output processing.

### **Instructions:**
* Create a terminal-based Python application for basic banking operations.
* Display a welcome message and menu options every time the program runs.
* Keep the program running until the user chooses to exit.
* Store all account data in text files inside an `accounts` folder (must be created manually in the same directory as the script).
* Use `with open()` (context manager) for all file operations.
* Do not use external modules such as `os`, `getpass`, or any third-party libraries.
* **Create Account**
  * Ask the user for an account holder name.
  * Ask the user to set a 4-digit PIN.
  * Validate that the PIN contains only digits and is exactly 4 characters long.
  * Create a new text file inside the `accounts` folder using the account holder name.
  * Prevent account creation if a file with the same name already exists.
  * Store the following information inside the account file:
    * Name
    * PIN
    * Balance (initially set to 0)
* **View Balance**
  * Ask the user for the account name.
  * Ask the user for the PIN.
  * Validate the entered PIN against the stored PIN.
  * Display the account holder name and current balance using formatted output with separators.
* **Deposit Money**
  * Ask the user for the account name and PIN.
  * Ask for the amount to deposit.
  * Ensure the deposit amount is a positive number.
  * Add the deposited amount to the existing balance.
  * Update the account file with the new balance.
  * Display a success message along with the updated balance.
* **Withdraw Money**
  * Ask the user for the account name and PIN.
  * Ask for the amount to withdraw.
  * Ensure the withdrawal amount is a positive number.
  * Check that the account has sufficient balance before withdrawing.
  * Deduct the amount from the balance and update the account file.
  * Display a success message along with the remaining balance.
* Display meaningful error messages for:
  * Invalid menu choices
  * Incorrect PIN
  * Invalid amounts
  * Missing account files

### **Sample Account File Format (For Reference):**
```
Name: Pralhad
PIN: 5656
Balance: 1000
```

### **Sample Output:**
```
========================================
   Welcome to Terminal Bank of India
========================================

========================================
Please select an option:
1. Create Account
2. View Balance
3. Deposit Money
4. Withdraw Money
5. Exit
========================================
Enter your choice (1-5): 2
 View Balance ---
Enter account name: Pralhad
Enter PIN: 5656
---------------------------
👤 Account Holder: Pralhad
💰 Current Balance: ₹1000
---------------------------
```