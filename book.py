#Book.py
import json
#Book class is used to create book objects with title, author. year and isbn attributes.
class Book:
    def __init__(self,title,author,year,isbn):#Initializing the attributes for book class
        self.title=title
        self.author=author
        self.year=year
        self.isbn=isbn
    def __str__(self): #This method is used to return a human-redable string of book's details
        return f"Title:{self.title}, Author:{self.author}, Year:{self.year}, ISBN:{self.isbn}"
    
    def to_dict(self):
        #Converts Book object to dictionary for JSON storage.
        return {"title": self.title, "author": self.author, "year": self.year, "isbn": self.isbn}
    
    @staticmethod
    def from_dict(data):
        #Creates a Book object from dictionary data
        return Book(data['title'], data['author'], data['year'], data['isbn'])
    