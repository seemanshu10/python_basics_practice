## 🎯 AP. Library Book System

### Task Objective

* Create a class to represent books in a library.
* Assign individual attributes to each book object.
* Define shared attributes across all book objects.
* Add functionality to display book info and update its status.
* Track how many total books are created in the system.

### Instructions

* Create a class named `Book` that stores `title`, `author`, and `status` (e.g., "available" or "checked out").
* Include a class attribute that tracks the total number of books created.
* Add a method that prints the book's current information (title, author, and status).
* Add a method that updates the book’s status (e.g., to `"checked out"` or `"available"`).
* After creating multiple book objects, print the class attribute that shows the total number of books in the system.
* Print the internal state of one book using the `__dict__` attribute.

### Sample Output

**Usage**

```python
# Create book objects
book1 = Book("1984", "George Orwell", "Available")
book2 = Book("Dune", "Frank Herbert", "Checked Out")

# Display info
book1.display_info()
book2.display_info()

# Update status
print("\nUpdating status of '1984'...")
book1.update_status("Checked Out")
book1.display_info()

# Display total books
print(f"\nTotal books in system: {Book.total_books}")

# Display internal state
print("\nInternal data for 'Dune':")
print(book2.__dict__)
```

**Output**

```
Book: '1984' by George Orwell | Status: Available
Book: 'Dune' by Frank Herbert | Status: Checked Out

Updating status of '1984'...
Book: '1984' by George Orwell | Status: Checked Out

Total books in system: 2

Internal data for 'Dune':
{'title': 'Dune', 'author': 'Frank Herbert', 'status': 'Checked Out'}
```
