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
