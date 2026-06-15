
# analytics.py

import csv
from collections import Counter

TRANSACTIONS_FILE = "data/transactions.csv"


def top_borrowed_books():
    """
    Returns a list of dictionaries:
    [
        {"book_id": "1", "count": 5},
        {"book_id": "2", "count": 3}
    ]
    """

    book_counter = Counter()

    try:
        with open(
            TRANSACTIONS_FILE,
            "r"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:
                book_counter[
                    row["book_id"]
                ] += 1

        results = []

        for (
            book_id,
            count
        ) in book_counter.most_common(10):

            results.append({
                "book_id": book_id,
                "count": count
            })

        return results

    except FileNotFoundError:

        return []


def monthly_analytics():
    """
    Returns a dictionary:
    {
        "total_borrowed": 10,
        "total_returned": 8,
        "total_fine": 50
    }
    """

    total_borrowed = 0
    total_returned = 0
    total_fine = 0

    try:

        with open(
            TRANSACTIONS_FILE,
            "r"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                total_borrowed += 1

                if row["return_date"]:
                    total_returned += 1

                try:
                    total_fine += int(
                        row["fine"]
                    )

                except (
                    ValueError,
                    TypeError
                ):
                    pass

        return {
            "total_borrowed":
                total_borrowed,

            "total_returned":
                total_returned,

            "total_fine":
                total_fine
        }

    except FileNotFoundError:

        return {
            "total_borrowed": 0,
            "total_returned": 0,
            "total_fine": 0
        }


