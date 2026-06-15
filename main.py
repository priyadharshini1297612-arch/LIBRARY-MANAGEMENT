

from library import (
    register_student,
    view_books,
    borrow_book,
    return_book,
    search_book,
    reserve_book,
    transaction_history
)

from chatbot import chatbot
from payment import upload_screenshot
from analytics import (
    top_borrowed_books,
    monthly_analytics
)
from report_generator import generate_pdf_report
from recommendation import recommend_book


ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"


def admin_login():

    username = input("Username: ")
    password = input("Password: ")

    if (
        username == ADMIN_USERNAME
        and
        password == ADMIN_PASSWORD
    ):

        print("\nLogin Successful")
        return True

    print("\nInvalid Credentials")
    return False


def recommendation_menu():

    interest = input(
        "\nEnter Interest: "
    )

    book = recommend_book(
        interest
    )

    print(
        f"\nRecommended Book: {book}"
    )


def main_menu():

    while True:

        print("\n")
        print("=" * 50)
        print("AI LIBRARY MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Admin Login")
        print("2. Student Registration")
        print("3. View Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Search Book")
        print("7. Reserve Book")
        print("8. AI Recommendation")
        print("9. AI Chatbot")
        print("10. Upload Payment Screenshot")
        print("11. Transaction History")
        print("12. Top Borrowed Books")
        print("13. Monthly Analytics")
        print("14. Generate PDF Report")
        print("15. Exit")

        choice = input(
            "\nEnter Choice: "
        )

        if choice == "1":

            admin_login()

        elif choice == "2":

            register_student()

        elif choice == "3":

            view_books()

        elif choice == "4":

            borrow_book()

        elif choice == "5":

            return_book()

        elif choice == "6":

            search_book()

        elif choice == "7":

            reserve_book()

        elif choice == "8":

            recommendation_menu()

        elif choice == "9":

            chatbot()

        elif choice == "10":

            upload_screenshot()

        elif choice == "11":

            transaction_history()

        elif choice == "12":

            top_borrowed_books()

        elif choice == "13":

            monthly_analytics()

        elif choice == "14":

            generate_pdf_report()

        elif choice == "15":

            print(
                "\nThank you for using the system."
            )
            break

        else:

            print(
                "\nInvalid Choice"
            )


if __name__ == "__main__":
    main_menu()
