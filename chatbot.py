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
# Library Rules (API format)
# -------------------------------
def get_library_rules():
    return [
        "Borrowed books must be returned within 7 days.",
        "Fine is ₹5 per overdue day.",
        "Handle books carefully.",
        "Lost books must be replaced.",
        "Student ID is required for borrowing.",
        "Reserved books must be collected within 2 days."
    ]

# -------------------------------
# Core chatbot logic
# -------------------------------
def process_message(user_message):

    user = user_message.lower().strip()

    # Greetings
    if user in ["hi", "hello"]:
        return {"response": "Hello! How can I help you today?"}

    # Help
    if "help" in user:
        return {
            "response": "Available commands",
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
        return {"response": "Please provide your interest (python, ai, data science etc.)"}

    if "python" in user and "book" in user:
        return {"response": "Recommended: Python Programming"}

    if "ai" in user and "book" in user:
        return {"response": "Recommended: Artificial Intelligence"}

    if "machine learning" in user:
        return {"response": "Recommended: Machine Learning"}

    if "data science" in user:
        return {"response": "Recommended: Data Science Basics"}

    # Library actions (delegated)
    if "show books" in user or "available books" in user:
        return {"response": view_books()}

    if "search" in user:
        return {"response": "Use /search API endpoint"}

    if "borrow" in user:
        return {"response": "Use /borrow API endpoint"}

    if "return" in user:
        return {"response": "Use /return API endpoint"}

    if "reserve" in user:
        return {"response": "Use /reserve API endpoint"}

    if "history" in user:
        return {"response": transaction_history()}

    if "fine" in user:
        return {"response": "Fine is ₹5 per day after due date."}

    if "rules" in user:
        return {"response": get_library_rules()}

    if "due date" in user:
        return {"response": "Books must be returned within 7 days."}

    if "lost book" in user:
        return {"response": "Lost books must be replaced or paid for."}

    return {
        "response": "I didn't understand your request. Type 'help' for options."
    }

# -------------------------------
# Flask Route (MAIN CHAT API)
# -------------------------------
@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    message = data.get("message", "")

    result = process_message(message)

    return jsonify({
        "user_message": message,
        "bot_response": result
    })

# -------------------------------
# Run Flask App
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
