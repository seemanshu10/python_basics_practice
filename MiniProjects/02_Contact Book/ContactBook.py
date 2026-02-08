"""
Objective:
In this task, you will:
Learn how to structure, search, update, and delete records stored in a text file.
Practice building a real-world utility that allows interaction with saved data.
Strengthen your ability to think through multiple user operations in a menu-based application.


Instructions:
Build a terminal-based Contact Book application that allows the user to:
Add new contacts
View all saved contacts
Search for a contact
Delete a contact
Exit the program
Use a folder named data (must be created manually in the same directory as the script).
Store contact information in a text file named contacts.txt inside the data folder.
Use with open() for all file operations.
Main Menu Options
Add New Contact
View All Contacts
Search Contact by Name
Delete Contact
Exit
Add New Contact
Ask the user to input:
Name
Phone Number
Email
Save the contact in contacts.txt using this format:
Name: Alice
Phone: 1234567890
Email: alice@example.com
---
Each contact block should be separated using ---.
View All Contacts
Read and display all contact blocks from the file.
If no contacts are available, show an appropriate message.
Search Contact by Name
Ask the user to enter a name.
Display the contact block that matches (case-insensitive).
If not found, show a “Contact not found” message.
Delete Contact
Ask the user to enter a name.
Remove the contact block that matches from the file.
Save the updated contact list back to the same file.
If no matching name is found, show an appropriate message.
Display appropriate messages for:
Invalid menu choices
Empty contact list
Errors in reading/writing the file
"""


CONTACT_BOOK_PATH = r"MiniProjects\02_Contact Book\data\contacts.txt"

# view all contacts in contact book 
def view_AllContacts():
    try:
        with open(CONTACT_BOOK_PATH,"r") as contactBook:    # open file 
            contactBookContent = contactBook.read().strip() # read file strip file 

        if not contactBookContent:
            print("No contacts available.")
            return
        
        print(contactBookContent)

    except FileNotFoundError:
        print("Error Reading the file.")

# search contact by name 
def search_ContactName():
    while True:
        try:
            name_toSearch = input("Enter name to search: ").strip().lower()
            # name to search in data stripping and lowercase the result 
            #print(name_toSearch)

            with open(CONTACT_BOOK_PATH,"r") as contactBook:
                contactBookContent = contactBook.read().split("---\n")
                print(contactBookContent)
                
            # ['Name: Alice\nPhone: 1234567890\nEmail: alice@example.com\n', 'Name: David\nPhone: 7820215463\nEmail: david@gmail.com\n', '']

            for contact in contactBookContent:
                # print(contact)
                if name_toSearch in contact.lower():
                    print("\nContact Found : ")
                    print(contact.strip())
                    return # exit when contact found 
                
            print("Contact not found .")

        except FileNotFoundError:
            print("Error Reading the file.")

        except KeyboardInterrupt:   # keyboardinterrupt error 
            print("Exiting Cleanly!")


# adding new contact in same file so will have to append 
def creating_Contact():
    try:
        # name input 
        name_Contact = input("Enter Name:").strip()

        # phone input taken 
        while True:
            try:
                phone_contact = int(input("Enter Phone Number: ").strip())
                break
            except ValueError:
                print("Phone Number Must be Digits.") 

        # email Input taken 
        email_account = input("Enter Email: ").strip()

        # adding new account in contactBook same file 
        with open(CONTACT_BOOK_PATH,"a") as contactBookNew:
            contactBookNew.write(f"Name: {name_Contact}\n")
            contactBookNew.write(f"Phone: {phone_contact}\n")
            contactBookNew.write(f"Email: {email_account}\n")
            contactBookNew.write("---\n")

        print("Contact Added Successfully.")

    except KeyboardInterrupt:   # keyboardinterrupt error 
        print("Exiting Cleanly!")
    except FileNotFoundError:
            print("Error Reading the file.")

# deleting the accoount details 

def delete_ContactName():
    try:
        while True:

            name_to_delete = input("Enter name to delete: ").strip().lower()

            if not name_to_delete:
                print("Name cannot be empty. Try Again.\n")
                continue
            
            with open(CONTACT_BOOK_PATH,"r") as contactBook:
                    contactBookContent = contactBook.read().split("---\n")

            updated_contacts = []
            contact_found = False

            for contact in contactBookContent:
                if name_to_delete in contact.lower():
                    contact_found = True
                else:
                    if contact.strip():
                        updated_contacts.append(contact)

            if not contact_found:
                print("Contact not found.Please try again!")
                continue

            with open(CONTACT_BOOK_PATH,"w") as contactBookDelete:
                for contact in updated_contacts:
                    contactBookDelete.write(contact.strip()+"\n---\n")

            print("Contact deleted successfully.")
            break # exirt loop after deleting 

    except KeyboardInterrupt:   # keyboardinterrupt error 
        print("Exiting Cleanly!")
    except FileNotFoundError:   # file not foundError 
        print("Error Reading the file.")

# displaying contact book options 
def contact_menu():
    title = "Contact Book"
    print("="*40)
    print(title.center(40)) # string method to centre the text 40 is total width of string agter centring  
    print("="*40)
    print("\n1. Add New Contact")
    print("2. View All Contact")
    print("3. Search Contact by Name")
    print("4. Delete Contact")
    print("5. Exit")
    print("=" * 40)


# display Choices for banking system 
def ContactBookSystem():
    try:
        while True:
            contact_menu()
            choice = input("\nEnter Your choice! (1-5): ") # choosing the user choice

            if choice == "1":
                creating_Contact()                                              # Creating new contact 
            elif choice == "2":
                view_AllContacts()                                              # view all contacts function
            elif choice == "3":
                search_ContactName()                                            # seacrching by contact name 
            elif choice == "4":
                delete_ContactName()                                            # deleting by name 
            elif choice == "5":
                print("Thank you for using the contact book system. Goodbye!")  # exiting 
                break
            else:
                print("Error:Invalid Menu Choice")

    except KeyboardInterrupt:   # keyBoardInterrupt error handle
        print("\n\nExiting the contact book system. Exiting Cleanly. Gooodbye!")

ContactBookSystem()