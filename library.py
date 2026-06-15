import csv
import os
from datetime import datetime

# -------------------------------
# FILE PATHS
# -------------------------------
BOOKS_FILE = "data/books.csv"
TRANSACTIONS_FILE = "data/transactions.csv"

# -------------------------------
# Ensure CSV exists
# -------------------------------
def init_files():

    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["book_id", "title", "author", "available"])

    if not os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["user", "book_id", "action", "date"])

# -------------------------------
# 1. View Books (LOGIC ONLY)
# -------------------------------
def view_books():

    books = []

    with open(BOOKS_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            books.append(row)

    return books

# -------------------------------
# 2. Search Book
# -------------------------------
def search_book(query):

    results = []

    with open(BOOKS_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if query.lower() in row["title"].lower() or query.lower() in row["author"].lower():
                results.append(row)

    return results

# -------------------------------
# 3. Borrow Book
# -------------------------------
def borrow_book(user, book_id):

    books = []
    found = False

    with open(BOOKS_FILE, "r") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames

        for row in reader:
            if row["book_id"] == str(book_id) and row["available"] == "Yes":
                row["available"] = "No"
                found = True

            books.append(row)

    if not found:
        return {"error": "Book not available"}

    with open(BOOKS_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)

    log_transaction(user, book_id, "borrow")

    return {"message": "Book borrowed successfully"}

# -------------------------------
# 4. Return Book
# -------------------------------
def return_book(user, book_id):

    books = []

    with open(BOOKS_FILE, "r") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames

        for row in reader:
            if row["book_id"] == str(book_id):
                row["available"] = "Yes"

            books.append(row)

    with open(BOOKS_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)

    log_transaction(user, book_id, "return")

    return {"message": "Book returned successfully"}

# -------------------------------
# 5. Reserve Book
# -------------------------------
def reserve_book(user, book_id):

    log_transaction(user, book_id, "reserve")

    return {"message": "Book reserved successfully"}

# -------------------------------
# 6. Transaction History
# -------------------------------
def transaction_history():

    data = []

    with open(TRANSACTIONS_FILE, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            data.append(row)

    return data

# -------------------------------
# LOG TRANSACTION
# -------------------------------
def log_transaction(user, book_id, action):

    with open(TRANSACTIONS_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            user,
            book_id,
            action,
            datetime.now().date()
        ])
