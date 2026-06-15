pip install reportlab
# report_generator.py

import csv

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

TRANSACTIONS_FILE = (
    "data/transactions.csv"
)


def generate_pdf_report():

    pdf = SimpleDocTemplate(
        "Library_Report.pdf"
    )

    styles = (
        getSampleStyleSheet()
    )

    content = []

    title = Paragraph(
        "AI Library Management Report",
        styles["Title"]
    )

    content.append(title)

    content.append(
        Spacer(1, 12)
    )

    with open(
        TRANSACTIONS_FILE,
        "r"
    ) as file:

        reader = csv.reader(
            file
        )

        for row in reader:

            text = Paragraph(
                str(row),
                styles["BodyText"]
            )

            content.append(
                text
            )

    pdf.build(
        content
    )

    print(
        "PDF Report Generated Successfully"
    )
