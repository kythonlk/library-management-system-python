import os

class Book:
    BOOK_FILE = "book.txt"

    def __init__(self, isbn, title, format, subject, rental_price, num_copies):
        self.isbn = isbn
        self.title = title
        self.format = format
        self.subject = subject
        self.rental_price = rental_price
        self.num_copies = num_copies
        self.is_available = True

    def __str__(self):
        return f"{self.title} (ISBN: {self.isbn})"

    @staticmethod
    def add_book():
        isbn = input("Enter ISBN: ")
        title = input("Enter title: ")
        format = input("Enter format (Hardcover/Paperback): ")
        subject = input("Enter subject (Science/History/Literature): ")
        rental_price = input("Enter rental price per day: ")
        num_copies = input("Enter number of copies: ")

        with open(Book.BOOK_FILE, "a") as f:
            f.write(f"[{isbn},{title},{format},{subject},{rental_price},{num_copies},]\n")

        print(f"Book {title} added successfully.")

    @staticmethod
    def remove_book():
        title = input("Enter title: ")

        with open(Book.BOOK_FILE, "r") as f:
            lines = f.readlines()

        with open(Book.BOOK_FILE, "w") as f:
            removed = False
            for line in lines:
                if line.split(",")[1] == title:
                    removed = True
                else:
                    f.write(line)

            if not removed:
                print(f"Book {title} not found.")
            else:
                print(f"Book {title} removed successfully.")

    @staticmethod
    def update_book():
        title = input("Enter title: ")

        with open(Book.BOOK_FILE, "r") as f:
            lines = f.readlines()

        with open(Book.BOOK_FILE, "w") as f:
            updated = False
            for line in lines:
                if line.split(",")[1] == title:
                    updated = True
                    isbn = input(f"Enter new ISBN (current: {line.split(',')[0]}): ")
                    format = input(f"Enter new format (current: {line.split(',')[2]}): ")
                    subject = input(f"Enter new subject (current: {line.split(',')[3]}): ")
                    rental_price = input(f"Enter new rental price per day (current: {line.split(',')[4]}): ")
                    num_copies = input(f"Enter new number of copies (current: {line.split(',')[5]}): ")
                    f.write(f"[{isbn},{title},{format},{subject},{rental_price},{num_copies},]\n")
                else:
                    f.write(line)
            if not updated:
                print(f"Book {title} not found.")
            else:
                print(f"Book {title} updated successfully.")

    @staticmethod
    def view_available_books():
        print("\nAvailable Books:\n================")
        with open("book.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)

    @staticmethod
    def view_book_by_search(search):
        with open('book.txt', 'r') as file:
            for line in file:
                if search.lower() in line.lower():
                    print(line.strip())
