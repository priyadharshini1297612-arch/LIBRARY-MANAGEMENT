import csv
import os
from datetime import datetime

# -------------------------------
# CONFIG
# -------------------------------
PAYMENTS_FOLDER = "payments"
PAYMENTS_FILE = "data/payments.csv"

# -------------------------------
# Ensure folder exists
# -------------------------------
def create_payment_folder():
    if not os.path.exists(PAYMENTS_FOLDER):
        os.makedirs(PAYMENTS_FOLDER)

# -------------------------------
# Generate Payment ID
# -------------------------------
def generate_payment_id():
    try:
        with open(PAYMENTS_FILE, "r") as file:
            rows = list(csv.reader(file))
            return len(rows)
    except:
        return 1

# -------------------------------
# 1. Upload Payment (LOGIC ONLY)
# -------------------------------
def upload_payment(student_id, amount, screenshot_name):

    create_payment_folder()

    if not student_id or not amount or not screenshot_name:
        return {"error": "Missing required fields"}

    payment_id = generate_payment_id()

    file_exists = os.path.exists(PAYMENTS_FILE)

    with open(PAYMENTS_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "payment_id",
                "student_id",
                "amount",
                "screenshot",
                "status",
                "date"
            ])

        writer.writerow([
            payment_id,
            student_id,
            amount,
            screenshot_name,
            "Pending",
            datetime.now().date()
        ])

    return {
        "message": "Payment uploaded successfully",
        "payment_id": payment_id,
        "status": "Pending"
    }

# -------------------------------
# 2. Verify Payment
# -------------------------------
def verify_payment(payment_id):

    rows = []
    found = False

    with open(PAYMENTS_FILE, "r") as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            if row[0] == str(payment_id):
                row[4] = "Verified"
                found = True
            rows.append(row)

    with open(PAYMENTS_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

    if found:
        return {"message": "Payment Verified Successfully"}
    else:
        return {"error": "Payment ID Not Found"}

# -------------------------------
# 3. Payment History
# -------------------------------
def payment_history():

    data = []

    if not os.path.exists(PAYMENTS_FILE):
        return {"error": "No payment records found"}

    with open(PAYMENTS_FILE, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            data.append(row)

    return data

# -------------------------------
# 4. Payment Status
# -------------------------------
def payment_status(payment_id):

    if not os.path.exists(PAYMENTS_FILE):
        return {"error": "No payment records found"}

    with open(PAYMENTS_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["payment_id"] == str(payment_id):
                return {
                    "payment_id": payment_id,
                    "status": row["status"]
                }

    return {"error": "Payment Not Found"}
