import flask

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


@app.route("/contact-us/contact-modal")
def contact_modal():
    return render_template("/contact-us/contact-modal.html")


@app.route("/sitemap.xml")
def sitemap_index():
    xml_sitemap = flask.render_template("sitemap/sitemap-index.xml")
    response = flask.make_response(xml_sitemap)
    response.headers["Content-Type"] = "application/xml"

    return response
