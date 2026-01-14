import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

DATABASE = "database.db"


# ---------- DATABASE SETUP ----------
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT NOT NULL,
            email TEXT NOT NULL,
            room_type TEXT NOT NULL,
            check_in TEXT NOT NULL,
            check_out TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# Run DB setup on app start
init_db()


# ---------- ROUTES ----------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/booking")
def booking():
    return render_template("booking.html")


@app.route("/submit_booking", methods=["POST"])
def submit_booking():
    fullname = request.form["fullname"]
    email = request.form["email"]
    room_type = request.form["room_type"]
    check_in = request.form["check_in"]
    check_out = request.form["check_out"]

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO bookings (fullname, email, room_type, check_in, check_out)
        VALUES (?, ?, ?, ?, ?)
    """, (fullname, email, room_type, check_in, check_out))

    conn.commit()
    conn.close()

    return render_template("success.html", fullname=fullname)


# ---------- RUN APP ----------
if __name__ == "__main__":
    app.run(debug=True)
