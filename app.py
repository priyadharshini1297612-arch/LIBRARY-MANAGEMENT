from flask import Flask, jsonify, request
import csv
import os

# IMPORTANT: must exist BEFORE any routes
app = Flask(__name__)

# -------------------------------
# FILE PATHS
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

BOOKS_FILE = os.path.join(DATA_DIR, "books.csv")
STUDENTS_FILE = os.path.join(DATA_DIR, "students.csv")

# -------------------------------
# SAFE INIT FILES (Vercel FIXED)
# -------------------------------
def initialize_files():

    try:
        os.makedirs(DATA_DIR, exist_ok=True)

        # books.csv
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

        # students.csv
        if not os.path.exists(STUDENTS_FILE):
            with open(STUDENTS_FILE, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["student_id", "name", "email"])

    except Exception as e:
        print("Init error:", e)

# Run once safely
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

    try:
        books_list = []

        if not os.path.exists(BOOKS_FILE):
            return jsonify([])

        with open(BOOKS_FILE, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                books_list.append(row)

        return jsonify(books_list)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -------------------------------
# REGISTER STUDENT
# -------------------------------
@app.route("/register", methods=["POST"])
def register():

    try:
        data = request.get_json()

        student_id = data.get("student_id")
        name = data.get("name")
        email = data.get("email")

        if not all([student_id, name, email]):
            return jsonify({"error": "Missing fields"}), 400

        with open(STUDENTS_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([student_id, name, email])

        return jsonify({"message": "Student registered successfully"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -------------------------------
# SAFE PLACEHOLDER ROUTES
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
# DO NOT add app.run()
