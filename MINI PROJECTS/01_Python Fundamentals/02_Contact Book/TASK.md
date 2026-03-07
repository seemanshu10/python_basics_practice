## **PA. Contact Book**

### **Objective:**
* In this task, you will:
  * Learn how to structure, search, update, and delete records stored in a text file.
  * Practice building a real-world utility that allows interaction with saved data.
  * Strengthen your ability to think through multiple user operations in a menu-based application.

### **Instructions:**
* Build a terminal-based Contact Book application that allows the user to:
  * Add new contacts
  * View all saved contacts
  * Search for a contact
  * Delete a contact
  * Exit the program
* Use a folder named `data` (must be created manually in the same directory as the script).
* Store contact information in a text file named `contacts.txt` inside the `data` folder.
* Use `with open()` for all file operations.
* **Main Menu Options**
  * Add New Contact
  * View All Contacts
  * Search Contact by Name
  * Delete Contact
  * Exit
* **Add New Contact**
  * Ask the user to input:
    * Name
    * Phone Number
    * Email
  * Save the contact in `contacts.txt` using this format:
    ```
    Name: Alice
    Phone: 1234567890
    Email: alice@example.com
    ---
    ```
  * Each contact block should be separated using `---`.
* **View All Contacts**
  * Read and display all contact blocks from the file.
  * If no contacts are available, show an appropriate message.
* **Search Contact by Name**
  * Ask the user to enter a name.
  * Display the contact block that matches (case-insensitive).
  * If not found, show a “Contact not found” message.
* **Delete Contact**
  * Ask the user to enter a name.
  * Remove the contact block that matches from the file.
  * Save the updated contact list back to the same file.
  * If no matching name is found, show an appropriate message.
* Display appropriate messages for:
  * Invalid menu choices
  * Empty contact list
  * Errors in reading/writing the file

### **Sample Contact File Format (`contacts.txt`):**
```
Name: Alice
Phone: 1234567890
Email: alice@example.com

Name: Bob
Phone: 9876543210
Email: bob@example.com
```

### **Sample Output (Terminal):**
```
====================================
         📇 Contact Book
====================================

1. Add New Contact
2. View All Contacts
3. Search Contact by Name
4. Delete Contact
5. Exit

Enter your choice (1-5): 1
 Add New Contact ---
Enter name: Alice
Enter phone number: 1234567890
Enter email: alice@example.com
✅ Contact saved successfully!
```