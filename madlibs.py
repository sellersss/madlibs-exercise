from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello Worlds"


if __name__ == "__main__":
    """Debug mode/development server"""

    app.run(debug=True, host="0.0.0.0")