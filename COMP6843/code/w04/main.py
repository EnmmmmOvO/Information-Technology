from argon2 import PasswordHasher
from flask import Flask, abort, redirect, render_template, request, session
import db
import sqlite3

app = Flask(__name__)
app.secret_key = "cool-secret-key"
ph = PasswordHasher()



# USERS = {
#     "HamishWHC": {
#         "role": "user",
#         "password": "$argon2id$v=19$m=65536,t=3,p=4$14gM9oLtre3L4bQ0S/7BDQ$SjXIF2XWwef+EY2LQZRZLwBKbLZLplqFLcPpKMD0vew",
#     },
#     "ssparrow4": {
#         "role": "user",
#         "password": "$argon2id$v=19$m=65536,t=3,p=4$14gM9oLtre3L4bQ0S/7BDQ$SjXIF2XWwef+EY2LQZRZLwBKbLZLplqFLcPpKMD0vew",
#     },
#     "TrashPanda": {
#         "role": "user",
#         "password": "$argon2id$v=19$m=65536,t=3,p=4$14gM9oLtre3L4bQ0S/7BDQ$SjXIF2XWwef+EY2LQZRZLwBKbLZLplqFLcPpKMD0vew",
#     },
#     "admin": {
#         "role": "user",
#         "password": "$argon2id$v=19$m=65536,t=3,p=4$14gM9oLtre3L4bQ0S/7BDQ$SjXIF2XWwef+EY2LQZRZLwBKbLZLplqFLcPpKMD0vew",
#     },
# }


@app.route("/")
def index():
    if session.get("username"):
        return render_template("home.html")
    return render_template("index.html")


@app.route("/users")
def users_list():
    query = "SELECT * FROM users"
    res = db.queryPlayer(query)
    return res

    # if session.get("role") != "admin":
    #     return abort(403)
    # return render_template("users.html", users=USERS)


def verify(hash, plaintext):
    try:
        return ph.verify(hash, plaintext)
    except Exception:
        return False


@app.route("/login", methods=["GET", "POST"])
def login():
    errors = []

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        
        query = "SELECT password, role FROM users WHERE username = '" + username + "'"

        res = db.queryPlayer(query)

        if res == None:
            errors.append("Incorrect username or password!")
            return render_template("login.html", errors=errors)
        
        res = res[0]

        db_password = res[0]
        db_role = res[1]
        
        
        if username is not None and verify(db_password, password):
            session["username"] = username
            session["role"] = db_role
            return redirect("/")

        errors.append("Incorrect username or password!")

    return render_template("login.html", errors=errors)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
