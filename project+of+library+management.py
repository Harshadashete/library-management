
# coding: utf-8

# In[1]:


class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author}"

    def check_availability(self):
        return self.is_available

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return f"{self.title} has been borrowed."
        else:
            return f"{self.title} is not available."

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return f"{self.title} has been returned."
        else:
            return f"{self.title} was not borrowed."

class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
    
    def list_books(self):
        book_strings = []
        for book in self.books:
            book_strings.append(str(book))
        
        return "\n".join(book_strings)

def main():
    library = Library()

    book1 = Book("Wings of Fire", "Dr.APJ Kalam and Arun Tiwari", "978-8-173-711466")
    book2 = Book("Magic of Thinking Big", "David Schwartz ", "978-1-78-504047-4")
    
     

    library.add_book(book1)
    library.add_book(book2)

    user1 = User("Abhay")
    user2 = User("Ram")

    print("Welcome to the Library Management System!")
    print("Available books:")
    print(library.list_books())

    print(f"\n{user1} tries to borrow {book1}:")
    print(book1.borrow_book())

    print(f"\n{user2} tries to borrow {book1}:")
    print(book1.borrow_book())

    print(f"\n{user1} returns {book1}:")
    print(book1.return_book())

    print("\nAvailable books:")
    print(library.list_books())

if __name__ == "__main__":
    main()

