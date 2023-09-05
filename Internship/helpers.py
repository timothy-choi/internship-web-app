"""Various helper functions."""
import uuid
import hashlib
import flask
import Internship


def p2_hash(p2_password, salt=uuid.uuid4().hex, algorithm="sha512"):
    """Compute the salted and hashed password."""
    hashed = hashlib.new(algorithm)
    salted_password = salt + p2_password
    hashed.update(salted_password.encode('utf-8'))
    hashed_password = hashed.hexdigest()
    return "$".join([algorithm, salt, hashed_password])

def login():
    """Handle login POST requests."""
    username = flask.request.form['username']
    p2_password = flask.request.form['password']

    # blank input
    if not username or not p2_password:
        flask.abort(400)

    # connect to database and query users
    cur = Internship.model.get_db().execute(
        "SELECT username, password "
        "FROM users "
        "WHERE username == ?",
        (username, )
    )
    user = cur.fetchone()

    if user is None:
        flask.abort(403)

    # check password
    idx_s1 = user['password'].index("$")
    idx_s2 = user['password'].index("$", idx_s1+1)
    algorithm = user['password'][:idx_s1]
    salt = user['password'][idx_s1+1:idx_s2]

    if p2_hash(p2_password, salt, algorithm) != user['password']:
        flask.abort(403)

    # set session cookie
    flask.session['username'] = username


def create():
    """Handle account creation POST requests."""
    username = flask.request.form['username']
    p2_password = flask.request.form['password']

    # blank input
    if username is None or p2_password is None:
        flask.abort(400)
    # connect to database and query users
    conn = Internship.model.get_db()
    cur = conn.execute(
        "SELECT COUNT(*) as ct "
        "FROM users "
        "WHERE username == ?",
        (username, )
    )

    # username already exists
    if cur.fetchone()['ct'] > 0:
        flask.abort(409)

    # insert user into database
    conn.execute(
        "INSERT INTO users(username, password) "
        "VALUES(?, ?)",
        (username, p2_hash(p2_password))
    )

    # set session cookie
    flask.session['username'] = username


def delete():
    """Handle account deletion POST requests."""
    # abort if user is not logged in
    if 'username' not in flask.session:
        flask.abort(403)

    username = flask.session['username']
    conn = Internship.model.get_db()

    # delete the user
    conn.execute(
        "DELETE FROM users "
        "WHERE username == ?",
        (username, )
    )

    # clear the session
    flask.session.clear()


def edit():
    """Handle account edit POST requests."""
    # abort if user is not logged in
    if 'username' not in flask.session:
        flask.abort(403)

    username = flask.session['username']
    conn = Internship.model.get_db()

    # update user with new info
    conn.execute(
        "UPDATE users "
        "SET "
        "fullname = ?, "
        "email = ?, "
        "filename = ? "
        "WHERE username == ?",
        (username)
    )
   


def password():
    """Handle change password POST requests."""
    # abort if user is not logged in
    if 'username' not in flask.session:
        flask.abort(403)
    username = flask.session['username']
    oldpass = flask.request.form['password']
    newpass = flask.request.form['new_password1']
    newpass2 = flask.request.form['new_password2']

    # blank input
    if oldpass is None or newpass is None or newpass2 is None:
        flask.abort(400)
    conn = Internship.model.get_db()

    # verify passwords
    cur = conn.execute(
        "SELECT password "
        "FROM users "
        "WHERE username = ?",
        (username, )
    )
    oldpass2 = cur.fetchone()['password']

    idx_s1 = oldpass2.index("$")
    idx_s2 = oldpass2.index("$", idx_s1+1)
    algorithm = oldpass2[:idx_s1]
    salt = oldpass2[idx_s1+1:idx_s2]

    if p2_hash(oldpass, salt, algorithm) != oldpass2:
        flask.abort(403)
    if newpass != newpass2:
        flask.abort(401)
    # update the password
    conn.execute(
        "UPDATE users "
        "SET password = ? "
        "WHERE username = ?",
        (p2_hash(newpass), username)
    )


# add a redirect function
def redirect(target):
    """Redirect to the target."""
    # redirect to target
    args = flask.request.args
    if 'target' in args and args['target'] is not None:
        target = args['target']
    return flask.redirect(target)
