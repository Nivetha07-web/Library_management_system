class Library:
    def __init__(self):
        self.books = {}  # Dictionary to store book information: {book_id: {"title": str, "author": str, "issued": bool}}
    
    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print(f"Book ID {book_id} already exists!")
        else:
            self.books[book_id] = {"title": title, "author": author, "issued": False}
            print(f"Book '{title}' added successfully!")
    
    def display_books(self):
        if not self.books:
            print("No books in the library!")
        else:
            print("Books in the Library:")
            for book_id, info in self.books.items():
                status = "Available" if not info["issued"] else "Issued"
                print(f"ID: {book_id}, Title: {info['title']}, Author: {info['author']}, Status: {status}")
    
    def issue_book(self, book_id):
        if book_id not in self.books:
            print(f"Book ID {book_id} does not exist!")
        elif self.books[book_id]["issued"]:
            print(f"Book ID {book_id} is already issued!")
        else:
            self.books[book_id]["issued"] = True
            print(f"Book ID {book_id} has been issued.")
    
    def return_book(self, book_id):
        if book_id not in self.books:
            print(f"Book ID {book_id} does not exist!")
        elif not self.books[book_id]["issued"]:
            print(f"Book ID {book_id} was not issued!")
        else:
            self.books[book_id]["issued"] = False
            print(f"Book ID {book_id} has been returned.")

# Main Program
def main():
    library = Library()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            library.add_book(book_id, title, author)
        elif choice == "2":
            library.display_books()
        elif choice == "3":
            book_id = input("Enter Book ID to Issue: ")
            library.issue_book(book_id)
        elif choice == "4":
            book_id = input("Enter Book ID to Return: ")
            library.return_book(book_id)
        elif choice == "5":
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()