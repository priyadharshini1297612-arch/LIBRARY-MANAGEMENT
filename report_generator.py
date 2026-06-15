import csv
import os

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# -------------------------------
# FILE PATHS
# -------------------------------
TRANSACTIONS_FILE = "data/transactions.csv"
OUTPUT_FILE = "Library_Report.pdf"

# -------------------------------
# Generate PDF Report (LOGIC ONLY)
# -------------------------------
def generate_pdf_report():

    pdf = SimpleDocTemplate(OUTPUT_FILE)
    styles = getSampleStyleSheet()

    content = []

    # Title
    title = Paragraph("AI Library Management Report", styles["Title"])
    content.append(title)
    content.append(Spacer(1, 12))

    # If file missing
    if not os.path.exists(TRANSACTIONS_FILE):
        content.append(Paragraph("No transaction data found.", styles["BodyText"]))
        pdf.build(content)
        return OUTPUT_FILE

    # Read CSV
    with open(TRANSACTIONS_FILE, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            text = Paragraph(str(row), styles["BodyText"])
            content.append(text)
            content.append(Spacer(1, 6))

    pdf.build(content)

    return OUTPUT_FILE
