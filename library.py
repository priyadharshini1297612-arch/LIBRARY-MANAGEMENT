import csv
import os
from datetime import datetime, timedelta

BOOKS_FILE = "data/books.csv"
STUDENTS_FILE = "data/students.csv"
TRANSACTIONS_FILE = "data/transactions.csv"
RESERVATIONS_FILE = "data/reservations.csv"


def initialize_files():
    os.makedirs("data", exist_ok=True)

    # books.csv
    if not os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "book_id",
                "title",
                "author",
                "available"
            ])

            writer.writerows([
                ["1", "Python Programming", "John Smith", "Yes"],
                ["2", "Machine Learning", "Andrew Ng", "Yes"],
                ["3", "Data Science Basics", "Alice Brown", "Yes"],
                ["4", "Artificial Intelligence", "Stuart Russell", "Yes"],
                ["5", "Deep Learning", "Ian Goodfellow", "Yes"]
            ])

    # students.csv
    if not os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "student_id",
                "name",
                "email"
            ])

    # transactions.csv
    if not os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, "w", newline="") as file:
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
        with open(RESERVATIONS_FILE, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "student_id",
                "book_id",
                "reservation_date"
            ])


def register_student(student_id, name, email):
    with open(STUDENTS_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            student_id,
            name,
            email
        ])

    return "Student Registered Successfully"


def get_books():
    books = []

    with open(BOOKS_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            books.append(row)

    return books


def search_book(keyword):
    keyword = keyword.lower()

    results = []

    with open(BOOKS_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if (
                keyword in row["title"].lower()
                or
                keyword in row["author"].lower()
            ):
                results.append(row)

    return results


def borrow_book(student_id, book_id):
    books = []

    available = False

    with open(BOOKS_FILE, "r") as file:
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
        return False, "Book Not Available"

    with open(BOOKS_FILE, "w", newline="") as file:
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

    due_date = borrow_date + timedelta(days=7)

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

    return (
        True,
        f"Book Borrowed Successfully. Due Date: {due_date.date()}"
    )


def return_book(book_id):
    rows = []

    fine = 0

    with open(TRANSACTIONS_FILE, "r") as file:
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
                        return_date - due_date
                    ).days * 5

                row[4] = str(
                    return_date.date()
                )

                row[5] = str(fine)

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

    with open(BOOKS_FILE, "r") as file:
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

    return f"Book Returned Successfully. Fine: ₹{fine}"


def reserve_book(student_id, book_id):
    reservation_date = datetime.now().date()

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

    return "Book Reserved Successfully"


def get_transaction_history():
    transactions = []

    with open(TRANSACTIONS_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            transactions.append(row)

    return transactions


def add_book(book_id, title, author):
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

    return "Book Added Successfully"


def remove_book(book_id):
    books = []

    with open(BOOKS_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["book_id"] != book_id:
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

    return "Book Removed Successfully"


def get_students():
    students = []

    with open(STUDENTS_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append(row)

    return students
