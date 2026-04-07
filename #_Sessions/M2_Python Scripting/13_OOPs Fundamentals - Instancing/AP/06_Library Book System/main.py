# Library Book System
class Book:
    # number of books class variable 
    number_of_books = 0

    def __init__(self, book_title, author_name, book_status):
        self.book_title = book_title
        self.author_name = author_name
        self.book_status = book_status
        Book.number_of_books += 1 

    def display_info(self):
        print(f"Book: {self.book_title} by {self.author_name} | Status: {self.book_status}")

    def update_status(self, book_status):
        self.book_status = book_status


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
print(f"\nTotal books in system: {Book.number_of_books}")

# Display internal state
print("\nInternal data for 'Dune':")
print(book2.__dict__)

# book2.__dict__['publisher'] = "TechPress"
# print(book2.__dict__)

"""
Book: 1984 by George Orwell | Status: Available
Book: Dune by Frank Herbert | Status: Checked Out

Updating status of '1984'...
Book: 1984 by George Orwell | Status: Checked Out

Total books in system: 2

Internal data for 'Dune':
{'book_title': 'Dune', 'author_name': 'Frank Herbert', 'book_status': 'Checked Out'}
"""