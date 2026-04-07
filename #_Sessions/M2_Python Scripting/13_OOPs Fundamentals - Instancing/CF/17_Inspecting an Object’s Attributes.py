class Book:
    def __init__(self, title, pages, author):
        self.title = title
        self.pages = pages
        self.author = author
        
# Create a Book object
book1 = Book("Python Basics", 250, "Alice")

# Inspect the attributes
print(book1.__dict__)   
#{'title': 'Python Basics', 'pages': 250, 'author': 'Alice'}