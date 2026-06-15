from recommendation import recommend_book
from library import (
    view_books,
    search_book,
    borrow_book,
    return_book,
    reserve_book,
    transaction_history
)

def show_help():

    print("\n===== AVAILABLE COMMANDS =====")

    print("recommend book")
    print("show books")
    print("search book")
    print("borrow book")
    print("return book")
    print("reserve book")
    print("transaction history")
    print("library rules")
    print("fine")
    print("help")
    print("exit")


def library_rules():

    print("\n===== LIBRARY RULES =====")

    print("1. Borrowed books must be returned within 7 days.")
    print("2. Fine is ₹5 per overdue day.")
    print("3. Handle books carefully.")
    print("4. Lost books must be replaced.")
    print("5. Student ID is required for borrowing.")
    print("6. Reserved books must be collected within 2 days.")


def chatbot():

    print("\n================================")
    print("AI LIBRARY ASSISTANT")
    print("================================")

    print("Type 'help' for available commands.")

    while True:

        user = input("\nYou: ").strip().lower()

        if user == "exit":

            print("Bot: Thank you for using the library system.")
            break

        elif user == "help":

            show_help()

        elif (
            "recommend" in user
            or
            "suggest" in user
        ):

            interest = input(
                "Bot: What topic are you interested in? "
            )

            book = recommend_book(
                interest
            )

            print(
                f"Bot: I recommend '{book}'."
            )

        elif (
            "python" in user
            and
            "book" in user
        ):

            print(
                "Bot: Recommended book: Python Programming"
            )

        elif (
            "ai" in user
            and
            "book" in user
        ):

            print(
                "Bot: Recommended book: Artificial Intelligence"
            )

        elif (
            "machine learning" in user
        ):

            print(
                "Bot: Recommended book: Machine Learning"
            )

        elif (
            "data science" in user
        ):

            print(
                "Bot: Recommended book: Data Science Basics"
            )

        elif (
            "show books" in user
            or
            "available books" in user
        ):

            view_books()

        elif (
            "search" in user
        ):

            search_book()

        elif (
            "borrow" in user
        ):

            print(
                "Bot: Starting borrow process..."
            )

            borrow_book()

        elif (
            "return" in user
        ):

            print(
                "Bot: Starting return process..."
            )

            return_book()

        elif (
            "reserve" in user
        ):

            print(
                "Bot: Starting reservation process..."
            )

            reserve_book()

        elif (
            "history" in user
        ):

            transaction_history()

        elif (
            "fine" in user
        ):

            print(
                "Bot: Fine is ₹5 per day after the due date."
            )

        elif (
            "rules" in user
        ):

            library_rules()

        elif (
            "due date" in user
        ):

            print(
                "Bot: Books must be returned within 7 days from the borrowing date."
            )

        elif (
            "lost book" in user
        ):

            print(
                "Bot: Lost books must be replaced or paid for according to library policy."
            )

        elif (
            "hello" in user
            or
            "hi" in user
        ):

            print(
                "Bot: Hello! How can I help you today?"
            )

        elif (
            "thank you" in user
            or
            "thanks" in user
        ):

            print(
                "Bot: You're welcome!"
            )

        else:

            print(
                """
Bot: I didn't understand that.

Try:
- recommend book
- show books
- search book
- borrow book
- return book
- reserve book
- fine
- library rules
- help
                """
            )
