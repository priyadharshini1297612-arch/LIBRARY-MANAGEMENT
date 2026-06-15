from flask import Flask, jsonify
import csv
from collections import Counter
import os

app = Flask(__name__)

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
@app.route("/analytics/top-books", methods=["GET"])
def top_borrowed_books():

    ensure_file()

    book_counter = Counter()

    with open(TRANSACTIONS_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["action"] == "borrow":
                book_counter[row["book_id"]] += 1

    top_books = book_counter.most_common(5)

    return jsonify({
        "top_borrowed_books": top_books
    })

# -------------------------------
# 2. User activity summary
# -------------------------------
@app.route("/analytics/user-activity", methods=["GET"])
def user_activity():

    ensure_file()

    user_counter = Counter()

    with open(TRANSACTIONS_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            user_counter[row["user"]] += 1

    activity = user_counter.most_common()

    return jsonify({
        "user_activity": activity
    })

# -------------------------------
# 3. Borrow vs Return stats
# -------------------------------
@app.route("/analytics/stats", methods=["GET"])
def stats():

    ensure_file()

    actions = Counter()

    with open(TRANSACTIONS_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            actions[row["action"]] += 1

    return jsonify({
        "borrow_count": actions.get("borrow", 0),
        "return_count": actions.get("return", 0),
        "reserve_count": actions.get("reserve", 0)
    })

# -------------------------------
# Run App
# -----------------------------
