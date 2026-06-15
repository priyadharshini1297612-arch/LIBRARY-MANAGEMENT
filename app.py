from flask import Flask, jsonify, request
import csv
import os

app = Flask(__name__)

# -------------------------------
# FILE PATHS
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

BOOKS_FILE = os.path.join(DATA_DIR, "books.csv")
STUDENTS_FILE = os.path.join(DATA_DIR, "students.csv")

# -------------------------------
# SAFE INIT FILES
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
            with open(STUDENTS_FILE, "w", newline="
