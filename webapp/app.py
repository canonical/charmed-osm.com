from canonicalwebteam.flask_base.app import FlaskBase
from flask import render_template

# Rename your project below
app = FlaskBase(
    __name__,
    "charmed-osm.com",
    template_folder="../templates",
    static_folder="../static",
    template_404="404.html",
    template_500="500.html",
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/osm-hackfests")
def hackfests():
    return render_template("osm-hackfests.html")


@app.route("/thank-you")
def thank_you():
    return render_template("thank-you.html")


@app.route("/contact-us")
def contact_us():
    return render_template("/contact-us/index.html")


@app.route("/contact-us/thank-you")
def contact_thanks_you():
    return render_template("/contact-us/thank-you.html")
