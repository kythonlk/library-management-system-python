from book import Book
from magazine import Magazine
from educational_dvd import EducationalDVD
from lecture_cd import LectureCD

while True:

    print("""
    ------------------------------------------
    ------------------------------------------
    Hello welcome to library management system
    ------------------------------------------
    ------------------------------------------
    """)

    print("""
    1. Add a new resource
    2. Remove a resource
    3. View currently available resources in each resource type
    4. View all resources (any type) search by filter
    5. Update a resource
    6. Exit
    ------------------------------------------------------------
    """)

    choice = input("Enter choice: ")

    if choice == "1":
        print("""
        1. book
        2. Magazine
        3. Educational DVD
        4. Lecture CD
        ------------------------------------------
        """)
        resource_type = input("Enter resource type: ")
        if resource_type == "1":
            Book.add_book()
        elif resource_type == "2":
            Magazine.add_magazine()
        elif resource_type == "3":
            EducationalDVD.add_dvd()
        elif resource_type == "4":
            LectureCD.add_lecturecd()
        else:
            print("Invalid choice")

    elif choice == "2":
        print("""
        1. book
        2. Magazine
        3. Educational DVD
        4. Lecture CD
        ------------------------------------------
        """)
        resource_type = input("Enter resource type: ")
        if resource_type == "1":
            Book.remove_book()
        elif resource_type == "2":
            Magazine.remove_magazine()
        elif resource_type == "3":
            EducationalDVD.remove_dvd()
        elif resource_type == "4":
            LectureCD.remove_lecturecd()
        else:
            print("Invalid choice")

    elif choice == "3":
        print("""
        1. Books
        2. Magazines
        3. Educational DVDs
        4. Lecture CDs
        ------------------------------------------
        """)
        resource_type = input("Enter resource type: ")
        if resource_type == "1":
            Book.view_available_books()
        elif resource_type == "2":
            Magazine.view_available_magazine()
        elif resource_type == "3":
            EducationalDVD.view_available_dvd()
        elif resource_type == "4":
            LectureCD.view_available_lecturecd()
        else:
            print("Invalid choice")

    elif choice == "4":
        print("""
        ---------------------------------------------------------------
        You can search all items of the library by title, subject ,etc.
        ---------------------------------------------------------------
        """)
        search = input("Enter search term to find: ")
        Book.view_book_by_search(search)
        Magazine.view_magazine_by_search(search)
        EducationalDVD.view_dvd_by_search(search)
        LectureCD.view_lecturecd_by_search(search)

    elif choice == "5":
        print("""
        1. book
        2. Magazine
        3. Educational DVD
        4. Lecture CD
        ------------------------------------------
        """)
        resource_type = input("Enter resource type: ")
        if resource_type == "1":
            Book.update_book()
        elif resource_type == "2":
            Magazine.update_magazine()
        elif resource_type == "3":
            EducationalDVD.update_dvd()
        elif resource_type == "4":
            LectureCD.update_lecturecd()
        else:
            print("Invalid choice")

    elif choice == '6':
        print("""
        --------------------------------------------------
        Thank you for using the library management system.
        --------------------------------------------------
        """)
        break

    else:
        print("Invalid input.")
