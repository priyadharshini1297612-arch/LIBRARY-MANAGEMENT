import csv
import os

# -------------------------------
# BOOK DATABASE
# -------------------------------
BOOK_DATABASE = {
    "python": [
        "Python Programming",
        "Advanced Python",
        "Automate the Boring Stuff with Python"
    ],
    "ai": [
        "Artificial Intelligence",
        "AI Foundations",
        "Modern Artificial Intelligence"
    ],
    "machine learning": [
        "Machine Learning",
        "Hands-On Machine Learning",
        "Practical Machine Learning"
    ],
    "deep learning": [
        "Deep Learning",
        "Neural Networks and Deep Learning",
        "Advanced Deep Learning"
    ],
    "data science": [
        "Data Science Basics",
        "Data Science from Scratch",
        "Data Analytics"
    ],
    "web development": [
        "HTML and CSS",
        "JavaScript Guide",
        "Flask Web Development"
    ],
    "cyber security": [
        "Cyber Security Essentials",
        "Ethical Hacking",
        "Network Security"
    ],
    "cloud": [
        "Cloud Computing",
        "AWS Fundamentals",
        "Cloud Architecture"
    ],
    "database": [
        "Database Systems",
        "SQL Complete Guide",
        "Database Design"
    ],
    "java": [
        "Java Programming",
        "Core Java",
        "Advanced Java"
    ],
    "c++": [
        "C++ Programming",
        "Object Oriented Programming in C++",
        "Advanced C++"
    ]
}

# -------------------------------
# Create books.csv if not exists
# -------------------------------
def create_books_csv():

    filename = "books.csv"

    if not os.path.exists(filename):

        books = [
            [1, "Python Programming", "John Smith", "Yes"],
            [2, "Machine Learning", "Andrew Ng", "Yes"],
            [3, "Data Science Basics", "Alice Brown", "Yes"],
            [4, "Artificial Intelligence", "Stuart Russell", "Yes"],
            [5, "Deep Learning", "Ian Goodfellow", "Yes"],
            [6, "Cyber Security Essentials", "Kevin Mitnick", "Yes"],
            [7, "Cloud Computing", "Thomas Erl", "Yes"],
            [8, "Database Systems", "Navathe", "Yes"],
            [9, "Java Programming", "Herbert Schildt", "Yes"],
            [10, "C++ Programming", "Bjarne Stroustrup", "Yes"]
        ]

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["book_id", "title", "author", "available"])
            writer.writerows(books)

# -------------------------------
# Recommendation Logic
# -------------------------------
def get_recommendations(interest):

    interest = interest.lower().strip()

    for topic, books in BOOK_DATABASE.items():
        if topic in interest:
            return books

    return [
        "Python Programming",
        "Machine Learning",
        "Data Science Basics"
    ]

# -------------------------------
# Single recommendation helper
# -------------------------------
def recommend_book(interest):

    books = get_recommendations(interest)

    return books[0]
