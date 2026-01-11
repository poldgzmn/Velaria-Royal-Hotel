from db_config import create_connection
from flask import Flask, render_template, request

app = Flask(__name__)

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

    conn = create_connection()
    if conn is None:
        return "Database connection failed", 500

    cursor = conn.cursor()

    sql = """
        INSERT INTO bookings (fullname, email, room_type, check_in, check_out)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (fullname, email, room_type, check_in, check_out))
    conn.commit()

    cursor.close()
    conn.close()

    return render_template("success.html", fullname=fullname)

if __name__ == "__main__":
    app.run(debug=True)
