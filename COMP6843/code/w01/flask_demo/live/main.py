from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    print(request.args)
    return "hello world!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
