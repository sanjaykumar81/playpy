from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self): pass


class MyBook(Book):

    def __init__(self, title, author, price):
        Book.__init__(self, title,author)
        self.price = price

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
        pass


if __name__ == "__main__":

    book = MyBook("life", "sanjay", "£34")
    book.display()