import flask 
import Internship

@Internship.app.route("/about/", methods=['GET'])
def get_about():
    context = {}
    return flask.render_template("about.html", **context)

@Internship.app.route("/contact/", methods=['GET'])
def get_contact():
    context = {}
    return flask.render_template("contact.html", **context)