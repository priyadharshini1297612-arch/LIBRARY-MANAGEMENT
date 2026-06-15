from flask import Flask, send_file
import csv

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

app = Flask(__name__)

TRANSACTIONS_FILE = "data/transactions.csv"
OUTPUT_FILE = "Library_Report.pdf"


def generate_pdf_report():

    pdf = SimpleDocTemplate(OUTPUT_FILE)
    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "AI Library Management Report",
        styles["Title"]
    )

    content.append(title)
    content.append(Spacer(1, 12))

    # Read CSV
    with open(TRANSACTIONS_FILE, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            text = Paragraph(str(row), styles["BodyText"])
            content.append(text)
            content.append(Spacer(1, 6))

    pdf.build(content)


# ---------------- FLASK ROUTES ----------------

@app.route("/")
def home():
    return "Library Report Generator is Running"


@app.route("/generate-report")
def generate_report():
    generate_pdf_report()
    return send_file(OUTPUT_FILE, as_attachment=True)


# ---------------- RUN APP ----------------

if __name__ == "__main__":
    app.run(debug=True)
