
from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

BOOKS_FILE = "data/books.csv"
STUDENTS_FILE = "data/students.csv"


def initialize_files():
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "book_id",
                "title",
                "author",
                "available"
            ])

            writer.writerows([
                ["1", "Python Programming", "John Smith", "Yes"],
                ["2", "Machine Learning", "Andrew Ng", "Yes"],
                ["3", "Data Science Basics", "Alice Brown", "Yes"],
                ["4", "Artificial Intelligence", "Stuart Russell", "Yes"],
                ["5", "Deep Learning", "Ian Goodfellow", "Yes"]
            ])

    if not os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "student_id",
                "name",
                "email"
            ])


initialize_files()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/books")
def books():
    books_list = []

    with open(BOOKS_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            books_list.append(row)

    return render_template(
        "books.html",
        books=books_list
    )


@app.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    if request.method == "POST":

        student_id = request.form["student_id"]

        name = request.form["name"]

        email = request.form["email"]

        with open(
            STUDENTS_FILE,
            "a",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                student_id,
                name,
                email
            ])

        return (
            "<h2>Student Registered Successfully</h2>"
            "<br><a href='/'>Back to Home</a>"
        )

    return render_template(
        "register.html"
    )


@app.route("/borrow")
def borrow():
    return (
        "<h2>Borrow Book page coming soon.</h2>"
        "<br><a href='/'>Back to Home</a>"
    )


@app.route("/return")
def return_book():
    return (
        "<h2>Return Book page coming soon.</h2>"
        "<br><a href='/'>Back to Home</a>"
    )


@app.route("/search")
def search():
    return (
        "<h2>Search Book page coming soon.</h2>"
        "<br><a href='/'>Back to Home</a>"
    )


@app.route("/reserve")
def reserve():
    return (
        "<h2>Reserve Book page coming soon.</h2>"
        "<br><a href='/'>Back to Home</a>"
    )


@app.route("/admin")
def admin():
    return (
        "<h2>Admin Login page coming soon.</h2>"
        "<br><a href='/'>Back to Home</a>"
    )


@app.route("/recommend")
def recommend():
    return (
        "<h2>AI Recommendation page coming soon.</h2>"
        "<br><a href='/'>Back to Home</a>"
    )


@app.route("/chatbot")
def chatbot():
    return (
        "<h2>AI Chatbot page coming soon.</h2>"
        "<br><a href='/'>Back to Home</a>"
    )


@app.route("/payment")
def payment():
    return (
        "<h2>Payment Upload page coming soon.</h2>"
        "<br><a href='/'>Back to Home</a>"
    )


@app.route("/history")
def history():
    return (
        "<h2>Transaction History page coming soon.</h2>"
        "<br><a href='/'>Back to Home</a>"
    )


@app.route("/analytics")
def analytics():
    return (
        "<h2>Analytics page coming soon.</h2>"
        "<br><a href='/'>Back to Home</a>"
    )


@app.route("/monthly")
def monthly():
    return (
        "<h2>Monthly Analytics page coming soon.</h2>"
        "<br><a href='/'>Back to Home</a>"
    )


@app.route("/report")
def report():
    return (
        "<h2>PDF Report page coming soon.</h2>"
        "<br><a href='/'>Back to Home</a>"
    )


if __name__ == "__main__":
    app.run(debug=True)





