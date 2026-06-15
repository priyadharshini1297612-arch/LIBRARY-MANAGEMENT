import csv
import os
from collections import Counter

# -------------------------------
# FILE PATH
# -------------------------------
TRANSACTIONS_FILE = "data/transactions.csv"

# -------------------------------
# Ensure file exists
# -------------------------------
def ensure_file():

    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["user", "book_id", "action", "date"])

# -------------------------------
# 1. Top borrowed books
# -------------------------------
def get_top_borrowed_books():

    ensure_file()

    book_counter = Counter()

    with open(TRANSACTIONS_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["action"] == "borrow":
                book_counter[row["book_id"]] += 1

    return book_counter.most_common(5)

# -------------------------------
# 2. User activity summary
# -------------------------------
def get_user_activity():

    ensure_file()

    user_counter = Counter()

    with open(TRANSACTIONS_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            user_counter[row["user"]] += 1

    return user_counter.most_common()

# -------------------------------
# 3. Borrow vs Return stats
# -------------------------------
def get_stats():

    ensure_file()

    actions = Counter()

    with open(TRANSACTIONS_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            actions[row["action"]] += 1

    return {
        "borrow_count": actions.get("borrow", 0),
        "return_count": actions.get("return", 0),
        "reserve_count": actions.get("reserve", 0)
    }
