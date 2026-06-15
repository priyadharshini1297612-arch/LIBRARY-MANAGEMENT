from flask import Flask, request, jsonify
from recommendation import recommend_book
from library import (
    view_books,
    search_book,
    borrow_book,
    return_book,
    reserve_book,
    transaction_history
)

app = Flask(__name__)

# -------------------------------
# Library Rules
# -------------------------------
def library_rules():
    return [
        "Borrowed books must be returned within 7 days.",
        "Fine is ₹5 per overdue day.",
        "Handle books carefully.",
        "Lost books must be replaced.",
        "Student ID is required for borrowing.",
        "Reserved books must be collected within 2 days."
    ]

# -------------------------------
# Chatbot Logic
# -------------------------------
def chatbot_response(user):

    user = user.lower().strip()

    # Greetings
    if user in ["hi", "hello"]:
        return "Hello! How can I help you today?"

    if "help" in user:
        return {
            "commands": [
                "recommend book",
                "show books",
                "search book",
                "borrow book",
                "return book",
                "reserve book",
                "transaction history",
                "library rules",
                "fine"
            ]
        }

    # Recommendation
    if "recommend" in user or "suggest" in user:
        return "Please send your interest (example: python, ai, data science)."

    if "python" in user and "book" in user:
        return "Recommended: Python Programming"

    if "ai" in user and "book" in user:
        return "Recommended: Artificial Intelligence"

    if "machine learning" in user:
        return "Recommended: Machine Learning"

    if "data science" in user:
        return "Recommended: Data Science Basics"

    # Library operations
    if "show books" in user or "available books" in user:
        return view_books()

    if "search" in user:
        return "Please use /search API endpoint"

    if "borrow" in user:
        return "Borrow process started. Use /borrow endpoint."

    if "return" in user:
        return "Return process started. Use /return endpoint."

    if "reserve" in user:
        return "Reservation process started. Use /reserve endpoint."

    if "history" in user:
        return transaction_history()

    if "fine" in user:
        return "Fine is ₹5 per day after due date."

    if "rules" in user:
        return library_rules()

    if "due date" in user:
        return "Books must be returned within 7 days."

    if "lost book" in user:
        return "Lost books must be replaced or compensated."

    return "I didn't understand. Try 'help' for commands."

# -------------------------------
# Flask Routes
# -------------------------------

@app.route("/")
def home():
    return "AI Library Chatbot Running"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    response = chatbot_response(user_message)

    return jsonify({
        "user": user_message,
        "bot": response
    })

# -------------------------------
# Run App
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
