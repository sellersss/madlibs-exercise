from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from madlibs import stories

app = Flask(__name__)
app.config["SECRET_KEY"] = "foobar"

debug = DebugToolbarExtension(app)


@app.route("/")
def index():
    """Display stories form"""

    return render_template("home.html")


@app.route("/form")
def form():
    """Display the required questions to complete story"""

    story_choice = request.args["story_choice"]
    story = stories[story_choice]

    title = story.title
    prompts = story.prompts

    return render_template(
        "form.html", title=title, prompts=prompts, story_choice=story_choice
    )


if __name__ == "__main__":
    """Debug mode/development server"""

    app.run(debug=True, host="0.0.0.0")