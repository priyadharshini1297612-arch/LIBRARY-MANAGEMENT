from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")




@app.route("/books")
def books():
    return "Display books here"


@app.route("/borrow")
def borrow():
    return "Borrow book page"


@app.route("/return")
def return_book():
    return "Return book page"


@app.route("/search")
def search():
    return "Search book page"


@app.route("/register")
def register():
    return "Student registration page"


@app.route("/recommend")
def recommend():
    return "AI recommendation page"


@app.route("/chatbot")
def chat():
    return "AI chatbot page"


@app.route("/payment")
def payment():
    return "Upload screenshot page"


@app.route("/history")
def history():
    return "Transaction history page"


@app.route("/analytics")
def analytics():
    return "Top borrowed books page"


@app.route("/monthly")
def monthly():
    return "Monthly analytics page"


@app.route("/report")
def report():
    return "Generate PDF report page"


@app.route("/admin")
def admin():
    return "Admin login page"
