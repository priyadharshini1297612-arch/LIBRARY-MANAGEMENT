import csv
import os

BOOKS_FILE = "data/books.csv"
STUDENTS_FILE = "data/students.csv"
TRANSACTIONS_FILE = "data/transactions.csv"
RESERVATIONS_FILE = "data/reservations.csv"


def initialize_files():

    os.makedirs("data", exist_ok=True)

    # books.csv
    if not os.path.exists(BOOKS_FILE):

        with open(
            BOOKS_FILE,
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "book_id",
                "title",
                "author",
                "available"
            ])

            writer.writerows([
                [
                    "1",
                    "Python Programming",
                    "John Smith",
                    "Yes"
                ],
                [
                    "2",
                    "Machine Learning",
                    "Andrew Ng",
                    "Yes"
                ],
                [
                    "3",
                    "Data Science Basics",
                    "Alice Brown",
                    "Yes"
                ],
                [
                    "4",
                    "Artificial Intelligence",
                    "Stuart Russell",
                    "Yes"
                ],
                [
                    "5",
                    "Deep Learning",
                    "Ian Goodfellow",
                    "Yes"
                ]
            ])

    # students.csv
    if not os.path.exists(STUDENTS_FILE):

        with open(
            STUDENTS_FILE,
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "student_id",
                "name",
                "email"
            ])

    # transactions.csv
    if not os.path.exists(TRANSACTIONS_FILE):

        with open(
            TRANSACTIONS_FILE,
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "student_id",
                "book_id",
                "borrow_date",
                "due_date",
                "return_date",
                "fine"
            ])

    # reservations.csv
    if not os.path.exists(RESERVATIONS_FILE):

        with open(
            RESERVATIONS_FILE,
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "student_id",
                "book_id",
                "reservation_date"
            ])

    print(
        "CSV files initialized successfully."
    )
 

def register_student():

    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    email = input("Enter Email: ")

    with open(
        STUDENTS_FILE,
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            student_id,
            name,
            email
        ])

    print("Student Registered Successfully")


def view_books():

    print("\nAVAILABLE BOOKS\n")

    with open(
        BOOKS_FILE,
        "r"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            print(
                f"Book ID: {row['book_id']}"
            )

            print(
                f"Title: {row['title']}"
            )

            print(
                f"Author: {row['author']}"
            )

            print(
                f"Available: {row['available']}"
            )

            print("-" * 30)


def search_book():

    keyword = input(
        "Enter Book Name or Author: "
    ).lower()

    found = False

    with open(
        BOOKS_FILE,
        "r"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            if (
                keyword in row["title"].lower()
                or
                keyword in row["author"].lower()
            ):

                found = True

                print(row)

    if not found:

        print("No Book Found")


def borrow_book():

    student_id = input(
        "Student ID: "
    )

    book_id = input(
        "Book ID: "
    )

    books = []

    available = False

    with open(
        BOOKS_FILE,
        "r"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            if (
                row["book_id"] == book_id
                and
                row["available"] == "Yes"
            ):

                row["available"] = "No"

                available = True

            books.append(row)

    if not available:

        print(
            "Book Not Available"
        )

        return

    with open(
        BOOKS_FILE,
        "w",
        newline=""
    ) as file:

        fieldnames = [
            "book_id",
            "title",
            "author",
            "available"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(books)

    borrow_date = datetime.now()

    due_date = borrow_date + timedelta(
        days=7
    )

    with open(
        TRANSACTIONS_FILE,
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            student_id,
            book_id,
            borrow_date.date(),
            due_date.date(),
            "",
            0
        ])

    print(
        f"Book Borrowed Successfully"
    )

    print(
        f"Due Date: {due_date.date()}"
    )


def return_book():

    book_id = input(
        "Enter Book ID: "
    )

    rows = []

    fine = 0

    with open(
        TRANSACTIONS_FILE,
        "r"
    ) as file:

        reader = csv.reader(file)

        header = next(reader)

        for row in reader:

            if (
                row[1] == book_id
                and
                row[4] == ""
            ):

                due_date = datetime.strptime(
                    row[3],
                    "%Y-%m-%d"
                )

                return_date = datetime.now()

                if return_date > due_date:

                    fine = (
                        return_date
                        -
                        due_date
                    ).days * 5

                row[4] = str(
                    return_date.date()
                )

                row[5] = str(
                    fine
                )

            rows.append(row)

    with open(
        TRANSACTIONS_FILE,
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(header)

        writer.writerows(rows)

    books = []

    with open(
        BOOKS_FILE,
        "r"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["book_id"] == book_id:

                row["available"] = "Yes"

            books.append(row)

    with open(
        BOOKS_FILE,
        "w",
        newline=""
    ) as file:

        fieldnames = [
            "book_id",
            "title",
            "author",
            "available"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(books)

    print(
        f"Book Returned"
    )

    print(
        f"Fine: ₹{fine}"
    )


def reserve_book():

    student_id = input(
        "Student ID: "
    )

    book_id = input(
        "Book ID: "
    )

    reservation_date = (
        datetime.now().date()
    )

    with open(
        RESERVATIONS_FILE,
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            student_id,
            book_id,
            reservation_date
        ])

    print(
        "Book Reserved Successfully"
    )


def transaction_history():

    print(
        "\nTRANSACTION HISTORY\n"
    )

    with open(
        TRANSACTIONS_FILE,
        "r"
    ) as file:

        reader = csv.reader(file)

        for row in reader:

            print(row)


def add_book():

    book_id = input(
        "Book ID: "
    )

    title = input(
        "Book Title: "
    )

    author = input(
        "Author: "
    )

    with open(
        BOOKS_FILE,
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            book_id,
            title,
            author,
            "Yes"
        ])

    print(
        "Book Added Successfully"
    )


def remove_book():

    book_id = input(
        "Enter Book ID: "
    )

    books = []

    with open(
        BOOKS_FILE,
        "r"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            if (
                row["book_id"]
                !=
                book_id
            ):

                books.append(row)

    with open(
        BOOKS_FILE,
        "w",
        newline=""
    ) as file:

        fieldnames = [
            "book_id",
            "title",
            "author",
            "available"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(books)

    print(
        "Book Removed Successfully"
    )


def view_students():

    print(
        "\nREGISTERED STUDENTS\n"
    )

    with open(
        STUDENTS_FILE,
        "r"
    ) as file:

        reader = csv.reader(file)

        for row in reader:

            print(row)
