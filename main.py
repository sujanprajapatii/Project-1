# main.py
import json
from book import Book
from library import Library

if __name__ == "__main__":
    library = Library()
    
    while True:
        print("\nPersonal Library Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = input("Enter year: ")
            isbn = input("Enter ISBN: ")
            library.add_book(Book(title, author, year, isbn))
            print("Book added successfully!")
        
        elif choice == "2":
            books = library.view_books()
            print("\nBooks in Library:")
            for book in books:
                print(book)
        
        elif choice == "3":
            keyword = input("Enter title or author to search: ")
            results = library.search_books(keyword)
            if results:
                print("\nSearch Results:")
                for book in results:
                    print(book)
            else:
                print("No matching books found.")
        
        elif choice == "4":
            isbn = input("Enter ISBN of book to update: ")
            new_title = input("Enter new title (leave blank to keep unchanged): ")
            new_author = input("Enter new author (leave blank to keep unchanged): ")
            new_year = input("Enter new year (leave blank to keep unchanged): ")
            if library.update_book(isbn, new_title or None, new_author or None, new_year or None):
                print("Book updated successfully!")
            else:
                print("Book not found.")
        
        elif choice == "5":
            isbn = input("Enter ISBN of book to delete: ")
            library.delete_book(isbn)
            print("Book deleted successfully!")
        
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
            
