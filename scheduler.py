# scheduler.py

import csv
import schedule
import time

from datetime import datetime

from email_service import (
    send_email
)

TRANSACTIONS_FILE = (
    "data/transactions.csv"
)

STUDENTS_FILE = (
    "data/students.csv"
)

BOOKS_FILE = (
    "data/books.csv"
)


def get_student_email(
        student_id):

    with open(
        STUDENTS_FILE,
        "r"
    ) as file:

        reader = csv.DictReader(
            file
        )

        for row in reader:

            if (
                row["student_id"]
                ==
                student_id
            ):

                return (
                    row["email"],
                    row["name"]
                )

    return None, None


def get_book_name(book_id):

    with open(
        BOOKS_FILE,
        "r"
    ) as file:

        reader = csv.DictReader(
            file
        )

        for row in reader:

            if (
                row["book_id"]
                ==
                book_id
            ):

                return row["title"]

    return "Unknown Book"


def check_due_books():

    today = (
        datetime.now().date()
    )

    with open(
        TRANSACTIONS_FILE,
        "r"
    ) as file:

        reader = csv.DictReader(
            file
        )

        for row in reader:

            if row["return_date"]:

                continue

            due_date = (
                datetime.strptime(
                    row["due_date"],
                    "%Y-%m-%d"
                ).date()
            )

            remaining = (
                due_date - today
            ).days

            if remaining <= 2:

                email, name = (
                    get_student_email(
                        row["student_id"]
                    )
                )

                book = (
                    get_book_name(
                        row["book_id"]
                    )
                )

                if email:

                    send_email(
                        email,
                        name,
                        book,
                        due_date
                    )


schedule.every().day.at(
    "09:00"
).do(check_due_books)

print(
    "Reminder Scheduler Running..."
)

while True:

    schedule.run_pending()

    time.sleep(60)
