import secrets

from flask import Flask, abort, g, make_response, render_template, request

app = Flask(__name__)

USERS = {
    "HamishWHC": {"balance": float(10000)},
    "TrashPanda": {"balance": float(0)},
}


@app.before_request
def before_request():
    g.username = request.cookies.get("username", None)
    if g.username is None:
        return "login by setting cookie 'username' to your username", 403
    g.user = USERS[g.username]


@app.route("/")
def index():
    return render_template("index.html", balance=g.user["balance"])


@app.route("/transfer", methods=["GET", "POST"])
def transfer():
    if request.method == "POST":
        # form_token = request.form.get("csrf_token")
        # cookie_token = request.cookies.get("csrf_token")
        # if form_token is None or cookie_token is None or form_token != cookie_token:
        #     abort(403, "missing or invalid CSRF token in form or cookie")

        to_user = USERS.get(request.form.get("to_user", ""))
        if to_user is None:
            abort(400, "missing or invalid 'to_user' field")

        try:
            amount = float(request.form.get("amount", "a"))
        except ValueError:
            abort(400, "missing or invalid 'amount' field")

        if amount <= 0:
            abort(400, "invalid 'amount' field")
        if amount > g.user["balance"]:
            abort(400, "you don't have that much money")

        g.user["balance"] -= amount
        to_user["balance"] += amount
        return "success"

    token = secrets.token_hex(64)
    response = make_response(render_template("transfer.html", csrf_token=token))
    response.set_cookie("csrf_token", token)
    return response


@app.route("/get-balance.js")
def get_balance():
    callback = request.args.get("callback", "alert")
    if not callback.isalnum():
        abort(400, "invalid callback")
    response = make_response(f"{callback}({g.user['balance']})")
    response.content_type = "application/javascript"
    return response


if __name__ == "__main__":
    app.run(debug=True, port=8082)
