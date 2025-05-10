from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    search = request.args.get("search")
    return "hello world!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
