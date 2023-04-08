class LectureCD:
    LECTURECD_FILE = "lecturecd.txt"

    def __init__(self, code, title, author, subject, rental_price, num_copies):
        self.code = code
        self.title = title
        self.author = author
        self.subject = subject
        self.rental_price = rental_price
        self.num_copies = num_copies
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author} ({self.code})"

    @staticmethod
    def add_lecturecd():
        code = input("Enter code: ")
        title = input("Enter title: ")
        author = input("Enter author: ")
        subject = input("Enter subject (Science/History/Literature): ")
        rental_price = input("Enter rental price per day: ")
        num_copies = input("Enter number of copies: ")

        with open(LectureCD.LECTURECD_FILE, "a") as f:
            f.write(f"[{code},{title},{author},{subject},{rental_price},{num_copies},]\n")

        print(f"Lecture CD {title} added successfully.")

    @staticmethod
    def remove_lecturecd():
        title = input("Enter title: ")

        with open(LectureCD.LECTURECD_FILE, "r") as f:
            lines = f.readlines()

        with open(LectureCD.LECTURECD_FILE, "w") as f:
            removed = False
            for line in lines:
                if line.split(",")[1] == title:
                    removed = True
                else:
                    f.write(line)

            if not removed:
                print(f"Lecture CD {title} not found.")
            else:
                print(f"Lecture CD {title} removed successfully.")

    @staticmethod
    def update_lecturecd():
        title = input("Enter title: ")

        with open(LectureCD.LECTURECD_FILE, "r") as f:
            lines = f.readlines()

        with open(LectureCD.LECTURECD_FILE, "w") as f:
            updated = False
            for line in lines:
                if line.split(",")[1] == title:
                    updated = True
                    code = input(f"Enter new code (current: {line.split(',')[0]}): ")
                    author = input(f"Enter new author (current: {line.split(',')[2]}): ")
                    subject = input(f"Enter new subject (current: {line.split(',')[3]}): ")
                    rental_price = input(f"Enter new rental price per day (current: {line.split(',')[4]}): ")
                    num_copies = input(f"Enter new number of copies (current: {line.split(',')[5]}): ")
                    f.write(f"[{code},{title},{author},{subject},{rental_price},{num_copies},]\n")
                else:
                    f.write(line)

            if not updated:
                print(f"Lecture CD {title} not found.")
            else:
                print(f"Lecture CD {title} updated successfully.")

    @staticmethod
    def view_available_lecturecd():
        print("\nAvailable lecture cd:\n================")
        with open("lecturecd.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)

    @staticmethod
    def view_lecturecd_by_search(search):
        with open('lecturecd.txt', 'r') as file:
            for line in file:
                if search.lower() in line.lower():
                    print(line.strip())


