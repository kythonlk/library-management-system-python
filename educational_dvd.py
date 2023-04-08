import os

class EducationalDVD:

    EDVD_FILE = "educational_dvd.txt"

    def __init__(self, dvd_number, title, subject, rental_price, num_copies):
        self.dvd_number = dvd_number
        self.title = title
        self.subject = subject
        self.rental_price = rental_price
        self.num_copies = num_copies

    def __str__(self):
        return f"{self.title} (dvd_number: {self.dvd_number})"
    
    @staticmethod
    def add_dvd():
        dvd_number = input("Enter DVD number: ")
        title = input("Enter title: ")
        subject = input("Enter subject: ")
        rental_price = float(input("Enter rental price per day: "))
        num_copies = int(input("Enter number of copies: "))

        with open(EducationalDVD.EDVD_FILE, "a") as f:
            f.write(f"[{dvd_number},{title},{subject},{rental_price},{num_copies},]\n")

        print(f"Educational DVD {title} added successfully.")

                
    @staticmethod
    def remove_dvd():
        title = input("Enter title: ")
        with open(EducationalDVD.EDVD_FILE, "r") as f:
            lines = f.readlines()
        with open(EducationalDVD.EDVD_FILE, "w") as f:
            removed = False
            for line in lines:
                if line.split(",")[1] == title:
                    removed = True
                else:
                    f.write(line)
            if not removed:
                print(f"Educational DVD {title} not found.")
            else:
                print(f"Educational DVD {title} removed successfully.")

    @staticmethod
    def update_dvd():
        title = input("Enter title: ")
        with open(EducationalDVD.EDVD_FILE, "r") as f:
            lines = f.readlines()
        with open(EducationalDVD.EDVD_FILE, "w") as f:
            updated = False
            for line in lines:
                if line.split(",")[1] == title:
                    updated = True
                    dvd_number = input(f"Enter new dvd_number (current: {line.split(',')[0]}): ")
                    subject = input(f"Enter new subject (current: {line.split(',')[1]}): ")
                    rental_price = input(f"Enter new rental price per day (current: {line.split(',')[3]}): ")
                    num_copies = input(f"Enter new number of copies (current: {line.split(',')[4]}): ")
                    f.write(f"[{dvd_number},{title},{subject},{rental_price},{num_copies},]\n")
                else:
                    f.write(line)
            if not updated:
                print(f"Book {title} not found.")
            else:
                print(f"Book {title} updated successfully.")

    @staticmethod
    def view_available_dvd():
        print("\nAvailable Educational DVD:\n================")
        with open("educational_dvd.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)

    @staticmethod
    def view_dvd_by_search(search):
        with open('educational_dvd.txt', 'r') as file:
            for line in file:
                if search.lower() in line.lower():
                    print(line.strip())
