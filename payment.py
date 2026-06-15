from flask import Flask, request, jsonify
import csv
import os
import shutil
from datetime import datetime

app = Flask(__name__)

# -------------------------------
# CONFIG
# -------------------------------
PAYMENTS_FOLDER = "payments"
PAYMENTS_FILE = "data/payments.csv"

# -------------------------------
# Create folder if not exists
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
# 1. Upload Payment Screenshot
# -------------------------------
@app.route("/upload-payment", methods=["POST"])
def upload_payment():

    create_payment_folder()

    data = request.get_json()

    student_id = data.get("student_id")
    amount = data.get("amount")
    screenshot_path = data.get("screenshot_path")

    if not student_id or not amount or not screenshot_path:
        return jsonify({"error": "Missing required fields"}), 400

    if not os.path.exists(screenshot_path):
        return jsonify({"error": "Screenshot file not found"}), 400

    payment_id = generate_payment_id()

    filename = f"payment_{payment_id}_{os.path.basename(screenshot_path)}"
    destination = os.path.join(PAYMENTS_FOLDER, filename)

    shutil.copy(screenshot_path, destination)

    # Save to CSV
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
            filename,
            "Pending",
            datetime.now().date()
        ])

    return jsonify({
        "message": "Payment uploaded successfully",
        "payment_id": payment_id,
        "status": "Pending"
    })

# -------------------------------
# 2. Verify Payment
# -------------------------------
@app.route("/verify-payment", methods=["POST"])
def verify_payment():

    data = request.get_json()
    payment_id = str(data.get("payment_id"))

    rows = []
    found = False

    with open(PAYMENTS_FILE, "r") as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            if row[0] == payment_id:
                row[4] = "Verified"
                found = True
            rows.append(row)

    with open(PAYMENTS_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

    if found:
        return jsonify({"message": "Payment Verified Successfully"})
    else:
        return jsonify({"error": "Payment ID Not Found"}), 404

# -------------------------------
# 3. Payment History
# -------------------------------
@app.route("/payment-history", methods=["GET"])
def payment_history():

    data = []

    if not os.path.exists(PAYMENTS_FILE):
        return jsonify({"error": "No payment records found"}), 404

    with open(PAYMENTS_FILE, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            data.append(row)

    return jsonify(data)

# -------------------------------
# 4. Check Payment Status
# -------------------------------
@app.route("/payment-status", methods=["GET"])
def payment_status():

    payment_id = request.args.get("payment_id")

    if not payment_id:
        return jsonify({"error": "payment_id required"}), 400

    if not os.path.exists(PAYMENTS_FILE):
        return jsonify({"error": "No payment records found"}), 404

    with open(PAYMENTS_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["payment_id"] == payment_id:
                return jsonify({
                    "payment_id": payment_id,
                    "status": row["status"]
                })

    return jsonify({"error": "Payment Not Found"}), 404

# -------------------------------
# RUN APP
# -------------------------------
