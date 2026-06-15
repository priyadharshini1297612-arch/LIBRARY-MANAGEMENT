# analytics.py

import csv
from collections import Counter


TRANSACTIONS_FILE = "data/transactions.csv"


def top_borrowed_books():

    book_counter = Counter()

    try:

        with open(
            TRANSACTIONS_FILE,
            "r"
        ) as file:

            reader = csv.DictReader(
                file
            )

            for row in reader:

                book_counter[
                    row["book_id"]
                ] += 1

        print(
            "\nTOP BORROWED BOOKS\n"
        )

        for book_id, count in (
            book_counter.most_common(10)
        ):

            print(
                f"Book ID: {book_id} | Borrowed: {count} times"
            )

    except FileNotFoundError:

        print(
            "Transaction file not found."
        )


def monthly_analytics():

    total_borrowed = 0
    total_returned = 0
    total_fine = 0

    try:

        with open(
            TRANSACTIONS_FILE,
            "r"
        ) as file:

            reader = csv.DictReader(
                file
            )

            for row in reader:

                total_borrowed += 1

                if row["return_date"]:

                    total_returned += 1

                try:

                    total_fine += int(
                        row["fine"]
                    )

                except:

                    pass

        print(
            "\nMONTHLY ANALYTICS\n"
        )

        print(
            f"Books Borrowed : {total_borrowed}"
        )

        print(
            f"Books Returned : {total_returned}"
        )

        print(
            f"Fine Collected : ₹{total_fine}"
        )

    except FileNotFoundError:

        print(
            "Transaction file not found."
        )
