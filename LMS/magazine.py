class Magazine:
    MAGAZINE_FILE = "magazine.txt"

    def __init__(self, mag_num, title, color_or_bw, subject, rental_price, num_copies):
        self.mag_num = mag_num
        self.title = title
        self.color_or_bw = color_or_bw
        self.subject = subject
        self.rental_price = rental_price
        self.num_copies = num_copies
        self.is_available = True

    def __str__(self):
        return f"{self.title} (Magazine Number: {self.mag_num})"

    @staticmethod
    def add_magazine():
        mag_num = input("Enter magazine number: ")
        title = input("Enter title: ")
        color_or_bw = input("Enter color or black&white print: ")
        subject = input("Enter subject (Science/Technology/Sports): ")
        rental_price = input("Enter rental price per day: ")
        num_copies = input("Enter number of copies: ")

        with open(Magazine.MAGAZINE_FILE, "a") as f:
            f.write(f"[{mag_num},{title},{color_or_bw},{subject},{rental_price},{num_copies},]\n")

        print(f"Magazine {title} added successfully.")

    @staticmethod
    def remove_magazine():
        title = input("Enter title: ")

        with open(Magazine.MAGAZINE_FILE, "r") as f:
            lines = f.readlines()

        with open(Magazine.MAGAZINE_FILE, "w") as f:
            removed = False
            for line in lines:
                if line.split(",")[1] == title:
                    removed = True
                else:
                    f.write(line)

            if not removed:
                print(f"Magazine {title} not found.")
            else:
                print(f"Magazine {title} removed successfully.")

    @staticmethod
    def update_magazine():
        title = input("Enter title: ")

        with open(Magazine.MAGAZINE_FILE, "r") as f:
            lines = f.readlines()

        with open(Magazine.MAGAZINE_FILE, "w") as f:
            updated = False
            for line in lines:
                if line.split(",")[1] == title:
                    updated = True
                    mag_num = input(f"Enter new magazine number (current: {line.split(',')[0]}): ")
                    color_or_bw = input(f"Enter new color or black&white print (current: {line.split(',')[2]}): ")
                    subject = input(f"Enter new subject (current: {line.split(',')[3]}): ")
                    rental_price = input(f"Enter new rental price per day (current: {line.split(',')[4]}): ")
                    num_copies = input(f"Enter new number of copies (current: {line.split(',')[5]}): ")
                    f.write(f"[{mag_num},{title},{color_or_bw},{subject},{rental_price},{num_copies},]\n")
                else:
                    f.write(line)

            if not updated:
                print(f"Magazine {title} not found.")
            else:
                print(f"Magazine {title} updated successfully.")

    @staticmethod
    def view_available_magazine():
        print("\nAvailable magazine:\n================")
        with open("magazine.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)

    @staticmethod
    def view_magazine_by_search(search):
        with open('magazine.txt', 'r') as file:
            for line in file:
                if search.lower() in line.lower():
                    print(line.strip())
