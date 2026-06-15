from flask import Flask, send_file, jsonify
import csv
import os

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

app = Flask(__name__)

# -------------------------------
# FILE PATH
# -------------------------------
TRANSACTIONS_FILE = "data/transactions.csv"
OUTPUT_FILE = "Library_Report.pdf"

# -------------------------------
# Generate PDF Report
# -------------------------------
def generate_pdf_report():

    pdf = SimpleDocTemplate(OUTPUT_FILE)
    styles = getSampleStyleSheet()

    content = []

    # Title
    title = Paragraph("AI Library Management Report", styles["Title"])
    content.append(title)
    content.append(Spacer(1, 12))

    # Check file exists
    if not os.path.exists(TRANSACTIONS_FILE):
        content.append(Paragraph("No transaction data found.", styles["BodyText"]))
        pdf.build(content)
        return

    # Read CSV data
    with open(TRANSACTIONS_FILE, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            text = Paragraph(str(row), styles["BodyText"])
            content.append(text)
            content.append(Spacer(1, 6))

    pdf.build(content)

# -------------------------------
# API: Download Report
# -------------------------------
@app.route("/generate-report", methods=["GET"])
def generate_report():

    generate_pdf_report()

    if not os.path.exists(OUTPUT_FILE):
        return jsonify({"error": "Report generation failed"}), 500

    return send_file(OUTPUT_FILE, as_attachment=True)

# -------------------------------
# Run App
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
