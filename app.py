from flask import Flask
import csv
import os

app = Flask(__name__)

# -------------------------------
# FOLDER PATH SETUP
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

BOOKS_FILE = os.path.join(DATA_DIR, "books.csv")


# -------------------------------
# HOME PAGE
# -------------------------------
@app.route("/")
def home():
    return """
    <h1>Library Management System</h1>
    <ul>
        <li><a href="/books">View Books</a></li>
    </ul>
    """


# -------------------------------
# BOOKS PAGE (SAFE VERSION)
# -------------------------------
@app.route("/books")
def books():
    books_html = """
    <h2>Books List</h2>
    <ul>
    """

    # If file not found → avoid crash
    if not os.path.exists(BOOKS_FILE):
        return """
        <h3>❌ books.csv not found inside data folder</h3>
        <a href="/">Back</a>
        """

    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                books_html += f"<li>Book ID: {row.get('book_id','N/A')} | Title: {row.get('title','N/A')} | Author: {row.get('author','N/A')}</li>"

        books_html += """
        </ul>
        <a href="/">Back</a>
        """

        return books_html

    except Exception as e:
        return f"<h3>❌ Error: {str(e)}</h3><a href='/'>Back</a>"


# -------------------------------
# RUN SERVER
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
