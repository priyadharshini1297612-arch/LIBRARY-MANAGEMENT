from flask import Flask
import csv
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

BOOKS_FILE = os.path.join(DATA_DIR, "books.csv")


@app.route("/")
def home():
    return """
    <h1>Library Management System</h1>
    <ul>
        <li><a href="/books">View Books</a></li>
    </ul>
    """


@app.route("/books")
def books():
    books_html = "<h2>Books List</h2><ul>"

    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                books_html += f"<li>{row}</li>"

    books_html += "</ul><a href='/'>Back</a>"
    return books_html


if __name__ == "__main__":
    app.run(debug=True)
