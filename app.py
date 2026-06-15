from flask import Flask, jsonify, render_template, request
import csv
import os

app = Flask(__name__)

# -------------------------------
# FILE PATHS
# -------------------------------
BOOKS_FILE = "data/books.csv"
STUDENTS_FILE = "data/students.csv"

# -------------------------------
# INIT FILES
# -------------------------------
def initialize_files():

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["book_id", "title", "author", "available"])
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
            writer.writerow(["student_id", "name", "email"])

initialize_files()

# -------------------------------
# HOME
# -------------------------------
@app.route("/")
def home():
    return jsonify({"status": "Library system running"})

# -------------------------------
# BOOKS
# -------------------------------
@app.route("/books")
def books():

    books_list = []

    with open(BOOKS_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            books_list.append(row)

    return jsonify(books_list)

# -------------------------------
# REGISTER STUDENT
# -------------------------------
@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    student_id = data.get("student_id")
    name = data.get("name")
    email = data.get("email")

    with open(STUDENTS_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, email])

    return jsonify({"message": "Student registered successfully"})

# -------------------------------
# PLACEHOLDER ROUTES (SAFE)
# -------------------------------
@app.route("/borrow")
def borrow():
    return jsonify({"message": "Borrow API coming soon"})

@app.route("/return")
def return_book():
    return jsonify({"message": "Return API coming soon"})

@app.route("/search")
def search():
    return jsonify({"message": "Search API coming soon"})

@app.route("/reserve")
def reserve():
    return jsonify({"message": "Reserve API coming soon"})

@app.route("/admin")
def admin():
    return jsonify({"message": "Admin API coming soon"})

@app.route("/recommend")
def recommend():
    return jsonify({"message": "Recommendation API coming soon"})

@app.route("/chatbot")
def chatbot():
    return jsonify({"message": "Chatbot API coming soon"})

@app.route("/payment")
def payment():
    return jsonify({"message": "Payment API coming soon"})

@app.route("/history")
def history():
    return jsonify({"message": "History API coming soon"})

@app.route("/analytics")
def analytics():
    return jsonify({"message": "Analytics API coming soon"})

@app.route("/report")
def report():
    return jsonify({"message": "Report API coming soon"})

# -------------------------------
# VERCEL ENTRY (IMPORTANT)
# -------------------------------
