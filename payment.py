# payment.py

import csv
import os
import shutil
from datetime import datetime

PAYMENTS_FOLDER = "payments"
PAYMENTS_FILE = "data/payments.csv"


def create_payment_folder():

    if not os.path.exists(
        PAYMENTS_FOLDER
    ):

        os.makedirs(
            PAYMENTS_FOLDER
        )


def generate_payment_id():

    try:

        with open(
            PAYMENTS_FILE,
            "r"
        ) as file:

            rows = list(
                csv.reader(file)
            )

            return (
                len(rows)
            )

    except:

        return 1


def upload_screenshot():

    create_payment_folder()

    student_id = input(
        "Enter Student ID: "
    )

    amount = input(
        "Enter Amount Paid: "
    )

    screenshot_path = input(
        "Enter Screenshot File Path: "
    )

    if not os.path.exists(
        screenshot_path
    ):

        print(
            "Screenshot file not found."
        )

        return

    payment_id = (
        generate_payment_id()
    )

    filename = (
        f"payment_{payment_id}_"
        +
        os.path.basename(
            screenshot_path
        )
    )

    destination = os.path.join(
        PAYMENTS_FOLDER,
        filename
    )

    shutil.copy(
        screenshot_path,
        destination
    )

    with open(
        PAYMENTS_FILE,
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            payment_id,
            student_id,
            amount,
            filename,
            "Pending",
            datetime.now().date()
        ])

    print(
        "Payment screenshot uploaded successfully."
    )

    print(
        f"Payment ID: {payment_id}"
    )

    print(
        "Verification Status: Pending"
    )


def verify_payment():

    payment_id = input(
        "Enter Payment ID: "
    )

    rows = []

    found = False

    with open(
        PAYMENTS_FILE,
        "r"
    ) as file:

        reader = csv.reader(file)

        header = next(reader)

        for row in reader:

            if row[0] == payment_id:

                row[4] = "Verified"

                found = True

            rows.append(row)

    with open(
        PAYMENTS_FILE,
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            header
        )

        writer.writerows(
            rows
        )

    if found:

        print(
            "Payment Verified Successfully"
        )

    else:

        print(
            "Payment ID Not Found"
        )


def payment_history():

    print(
        "\n===== PAYMENT HISTORY =====\n"
    )

    with open(
        PAYMENTS_FILE,
        "r"
    ) as file:

        reader = csv.reader(file)

        for row in reader:

            print(row)


def check_payment_status():

    payment_id = input(
        "Enter Payment ID: "
    )

    found = False

    with open(
        PAYMENTS_FILE,
        "r"
    ) as file:

        reader = csv.DictReader(
            file
        )

        for row in reader:

            if (
                row["payment_id"]
                ==
                payment_id
            ):

                found = True

                print(
                    f"Status: {row['status']}"
                )

                break

    if not found:

        print(
            "Payment Not Found"
        )


if __name__ == "__main__":

    while True:

        print("\n")
        print("1. Upload Screenshot")
        print("2. Verify Payment")
        print("3. Payment History")
        print("4. Check Payment Status")
        print("5. Exit")

        choice = input(
            "Enter Choice: "
        )

        if choice == "1":

            upload_screenshot()

        elif choice == "2":

            verify_payment()

        elif choice == "3":

            payment_history()

        elif choice == "4":

            check_payment_status()

        elif choice == "5":

            break

        else:

            print(
                "Invalid Choice"
            )
