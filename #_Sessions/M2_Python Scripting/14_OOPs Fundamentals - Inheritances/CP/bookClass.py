class Library:
    def __init__(self, name):
        self.name = name

    def show_library(self):
        print(f"Welcome to the {self.name} library.")

class Book(Library):
    def __init__(self, name, book_title):
        super().__init__(name)
        self.book_title = book_title
    
    def show_book(self):
        print(f"The book '{self.book_title}' is available in {self.name} library.")

library = Book("City Central", "1948")

library.show_library()
library.show_book()

"""
Welcome to the City Central library.
The book '1948' is available in City Central library.
"""