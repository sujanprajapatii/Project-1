# library.py
import json
from book import Book
class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_from_file()
    
    def add_book(self, book):
        #Adds a book to the library.
        self.books.append(book)
        self.save_to_file()
    
    def view_books(self):
        #Displays all books in the library.
        return [str(book) for book in self.books]
    
    def search_books(self, keyword):
        #Searches for books by title or author.
        return [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
    
    def update_book(self, isbn, new_title=None, new_author=None, new_year=None):
        #Updates a book's details.
        for book in self.books:
            if book.isbn == isbn:
                if new_title:
                    book.title = new_title
                if new_author:
                    book.author = new_author
                if new_year:
                    book.year = new_year
                self.save_to_file()
                return True
        return False
    
    def delete_book(self, isbn):
        #Deletes a book from the library.
        self.books = [book for book in self.books if book.isbn != isbn]
        self.save_to_file()
    
    def save_to_file(self):
        #Saves the library to a JSON file.
        with open(self.filename, 'w') as file:
            json.dump([book.to_dict() for book in self.books], file)
    
    def load_from_file(self):
        #Loads the library from a JSON file.
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.books = [Book.from_dict(book) for book in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []


