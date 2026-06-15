from flask import Flask, request, jsonify
import csv
import os
from datetime import datetime

app = Flask(__name__)

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
# 1. View Books
# -------------------------------
@app.route("/books", methods=["GET"])
def view_books():

    books = []

    with open(BOOKS_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            books.append(row)

    return jsonify(books)

# -------------------------------
# 2. Search Book
# -------------------------------
@app.route("/search", methods=["GET"])
def search_book():

    query = request.args.get("q", "").lower()

    results = []

    with open(BOOKS_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if query in row["title"].lower() or query in row["author"].lower():
                results.append(row)

    return jsonify(results)

# -------------------------------
# 3. Borrow Book
# -------------------------------
@app.route("/borrow", methods=["POST"])
def borrow_book():

    data = request.get_json()

    user = data.get("user")
    book_id = data.get("book_id")

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
        return jsonify({"error": "Book not available"}), 400

    with open(BOOKS_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)

    log_transaction(user, book_id, "borrow")

    return jsonify({
        "message": "Book borrowed successfully",
        "book_id": book_id,
        "user": user
    })

# -------------------------------
# 4. Return Book
# -------------------------------
@app.route("/return", methods=["POST"])
def return_book():

    data = request.get_json()

    user = data.get("user")
    book_id = data.get("book_id")

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

    return jsonify({
        "message": "Book returned successfully",
        "book_id": book_id,
        "user": user
    })

# -------------------------------
# 5. Reserve Book
# -------------------------------
@app.route("/reserve", methods=["POST"])
def reserve_book():

    data = request.get_json()

    user = data.get("user")
    book_id = data.get("book_id")

    log_transaction(user, book_id, "reserve")

    return jsonify({
        "message": "Book reserved successfully",
        "book_id": book_id,
        "user": user
    })

# -------------------------------
# 6. Transaction History
# -------------------------------
@app.route("/transactions", methods=["GET"])
def transaction_history():

    data = []

    with open(TRANSACTIONS_FILE, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            data.append(row)

    return jsonify(data)

# -------------------------------
# LOG TRANSACTIONS
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

# -------------------------------
# INIT + RUN
# -------------------------------
if __name__ == "__main__":
    init_files()
    app.run(debug=True)
