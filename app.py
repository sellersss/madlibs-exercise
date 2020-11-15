from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "foobar"

debug = DebugToolbarExtension(app)


@app.route("/")
def index():
    return render_template("home.html")


if __name__ == "__main__":
    """Debug mode/development server"""

    app.run(debug=True, host="0.0.0.0")