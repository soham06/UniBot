from flask import Flask, render_template, url_for, request, redirect, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/login")
def login_landing():
    return render_template("login.html")

@app.route("/uni-login")
def uni_login():
    return render_template("login-uni.html")

@app.route("/hs-login")
def hs_login():
    return render_template("login-hs.html")

@app.route("/register")
def register_landing():
    return render_template("register-landing.html")

@app.route("/uni-register")
def uni_register():
    return render_template("uni-register.html")

@app.route("/hs-register")
def hs_register():
    return render_template("hs-register.html")

@app.route("/homepage")
def landing_page():
    return render_template("universities.html")

@app.route("/programs")
def program():
    return render_template("programs.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

@app.route("/review")
def review():
    return render_template("review.html")

@app.route("/browse")
def browse():
    return render_template("profiles.html")

@app.route("/register-hs", methods=["GET", "POST"])
def register():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    if request.method=="POST":
        c.execute("""INSERT INTO hs_user (first, last, email, username, password, school, grade) \
            VALUES (?, ?, ?, ?, ?, ?, ?)""", 
        (request.form.get("first"), request.form.get("last"), request.form.get("email"),
        request.form.get("username"),generate_password_hash(request.form.get("password")), 
        request.form.get("school"), request.form.get("grade")))
        conn.commit()

    return redirect("/homepage")

@app.route("/register-uni", methods=["GET", "POST"])
def register_uni():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    if request.method=="POST":
        c.execute("""INSERT INTO uni_user (first, last, email, university, program, study_level, username, password) \
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", 
        (request.form.get("first"), request.form.get("last"), request.form.get("email"),
        request.form.get("university"), request.form.get("program"), request.form.get("level"),
        request.form.get("username"),generate_password_hash(request.form.get("password"))))
        conn.commit()

    return redirect("/homepage")

@app.route("/login-uni", methods=["GET", "POST"])
def login_uni():
    session.clear()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    if request.method == "POST":
        username = request.form.get("username")
        c.execute("SELECT * FROM uni_user WHERE username = ?", (username,))
        rows = c.fetchall() 
        if len(rows) != 1 or not check_password_hash(rows[0][6], request.form.get("password")):
            return "<h1>Incorrect Credentials</h1>"
        else:
            return redirect("/homepage")

@app.route("/login-hs", methods=["GET", "POST"])
def login_hs():
    session.clear()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    if request.method == "POST":
        username = request.form.get("username")
        c.execute("SELECT * FROM hs_user WHERE username = ?", (username,))
        rows = c.fetchall() 
        print(rows[0][5])
        if len(rows) != 1 or not check_password_hash(rows[0][4], request.form.get("password")):
            return "<h1>Incorrect Credentials</h1>"
        else:
            return redirect("/homepage")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.debug = True
    app.run()
