import flask
import Internship
from Internship.helpers import login, create, delete, edit, password, redirect


@Internship.app.route('/accounts/login/', methods=['GET'])
def show_login():
    """Display the login page."""
    # redirect if user is already logged in
    if 'username' in flask.session:
        return flask.redirect('/')
    # render the login page
    return flask.render_template("login.html")


@Internship.app.route('/accounts/logout/', methods=['POST'])
def logout():
    """Log the user out."""
    flask.session.clear()
    return flask.redirect(flask.url_for('show_login'))


@Internship.app.route('/accounts/create/', methods=['GET'])
def create_account():
    """Display page for account creation."""
    # redirect if user is already logged in
    if 'username' in flask.session:
        return flask.redirect(flask.url_for('edit_account'))
    # render the create account page
    return flask.render_template("create.html")


@Internship.app.route('/accounts/delete/', methods=['GET'])
def delete_account():
    """Display page for account deletion."""
    return flask.render_template("delete.html")


@Internship.app.route('/accounts/edit/', methods=['GET'])
def edit_account():
    """Display page for account editing."""
    # fetch fullname, email, and pfp of user
    cur = Internship.model.get_db().execute(
        "SELECT fullname, email, filename "
        "FROM users "
        "WHERE username == ?",
        (flask.session['username'], )
    )
    info = cur.fetchone()

    context = {"fullname": info["fullname"],
               "email": info["email"], "pfp": info["filename"]}
    return flask.render_template("edit.html", **context)


@Internship.app.route('/accounts/password/', methods=['GET'])
def change_password():
    """Display page for changing password."""
    return flask.render_template("password.html")


@Internship.app.route('/accounts/', methods=['POST'])
def accounts_post():
    """Handle POST requests related to accounts."""
    if flask.request.form['operation'] == 'login':
        login()
    elif flask.request.form['operation'] == 'create':
        create()
    elif flask.request.form['operation'] == 'delete':
        delete()
    elif flask.request.form['operation'] == 'edit_account':
        edit()
    elif flask.request.form['operation'] == 'update_password':
        password()
    else:
        flask.abort(400)

    # redirect to target
    return redirect('/')
