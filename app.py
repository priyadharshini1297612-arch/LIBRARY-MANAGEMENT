from flask import Flask, render_template
import os
import csv

app = Flask(__name__)

# -------------------------------
# FILE PATHS
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

BOOKS_FILE = os.path.join(DATA_DIR, "books.csv")
STUDENTS_FILE = os.path.join(DATA_DIR, "students.csv")
TRANSACTIONS_FILE = os.path.join(DATA_DIR, "transactions.csv")


# -------------------------------
# HOME PAGE
# -------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------------
# SHOW BOOKS
# -------------------------------
@app.route("/books")
def books():
    books_list = []

    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                books_list.append(row)

    return render_template("books.html", books=books_list)


# -------------------------------
# BORROW PAGE
# -------------------------------
@app.route("/borrow")
def borrow():
    return render_template("borrow.html")


# -------------------------------
# RETURN PAGE
# -------------------------------
@app.route("/return")
def return_book():
    return render_template("return.html")


# -------------------------------
# SEARCH PAGE
# -------------------------------
@app.route("/search")
def search():
    return render_template("search.html")


# -------------------------------
# RUN APP
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
