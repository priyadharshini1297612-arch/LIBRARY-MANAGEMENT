# email_service.py

import smtplib
from email.message import EmailMessage

# --------------------------
# CONFIGURATION
# --------------------------

SENDER_EMAIL = "yourlibrary@gmail.com"
APP_PASSWORD = "YOUR_APP_PASSWORD"


def send_email(receiver_email,
               student_name,
               book_name,
               due_date):

    try:

        msg = EmailMessage()

        msg["Subject"] = (
            "Library Book Return Reminder"
        )

        msg["From"] = SENDER_EMAIL

        msg["To"] = receiver_email

        message = f"""
Hello {student_name},

This is a reminder from the AI Library Management System.

Book Name : {book_name}

Due Date : {due_date}

Please return the book before the due date to avoid fines.

Fine Policy:
₹5 per day after the due date.

Thank You,
Library Management
"""

        msg.set_content(message)

        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465
        ) as smtp:

            smtp.login(
                SENDER_EMAIL,
                APP_PASSWORD
            )

            smtp.send_message(msg)

        print(
            f"Reminder sent to {receiver_email}"
        )

    except Exception as error:

        print(
            f"Email Error: {error}"
        )


def send_overdue_email(
        receiver_email,
        student_name,
        book_name,
        fine):

    try:

        msg = EmailMessage()

        msg["Subject"] = (
            "Overdue Book Notice"
        )

        msg["From"] = SENDER_EMAIL

        msg["To"] = receiver_email

        message = f"""
Hello {student_name},

The following borrowed book is overdue.

Book Name : {book_name}

Current Fine : ₹{fine}

Please return the book immediately.

Thank You,
Library Management
"""

        msg.set_content(message)

        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465
        ) as smtp:

            smtp.login(
                SENDER_EMAIL,
                APP_PASSWORD
            )

            smtp.send_message(msg)

        print(
            f"Overdue notice sent to {receiver_email}"
        )

    except Exception as error:

        print(
            f"Email Error: {error}"
        )


def test_email():

    receiver = input(
        "Enter Test Email: "
    )

    send_email(
        receiver,
        "Test Student",
        "Python Programming",
        "2026-06-25"
    )


if __name__ == "__main__":

    test_email()
