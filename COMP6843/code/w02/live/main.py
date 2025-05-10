from argon2 import PasswordHasher
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "cool-secret-key"
ph = PasswordHasher()


@app.route("/")
def index():
    if session.get("username"):
        return render_template("home.html")
    return render_template("index.html")


USERS = {
    "admin": {
        "password": "$argon2id$v=19$m=65536,t=3,p=4$14gM9oLtre3L4bQ0S/7BDQ$SjXIF2XWwef+EY2LQZRZLwBKbLZLplqFLcPpKMD0vew"
    }
}


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
        user = USERS.get(username)
        if user is not None and verify(user["password"], password):
            session["username"] = username
            return redirect("/")

        errors.append("Incorrect username or password!")

    return render_template("login.html", errors=errors)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
