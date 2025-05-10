from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "cool-secret-key"


@app.route("/")
def index():
    if session.get("username"):
        return render_template("home.html")
    else:
        return render_template("index.html")


USERS = {"admin": {"password": "admin"}}


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("username"):
        return redirect("/")

    errors = []

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        user = USERS.get(username)
        if user is not None and password == user["password"]:
            session["username"] = username
            return redirect("/")

        errors.append("Incorrect username or password.")

    return render_template("login.html", errors=errors)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
