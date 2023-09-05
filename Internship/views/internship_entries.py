import flask 
import Internship
from Internship.helpers import redirect

#Here's is my Flask implementation without the queries for getting/adding/deleting internship postings. 
#Feel free to edit or remove parts that you think are not necessary or wrong.

def process_post(curr_post, connection):
    #get all ratings from ratings table associated with the internship posting
    print(curr_post)
    cur = connection.execute(
        """
        SELECT fullname, rating 
        FROM ratings
        WHERE ratings.jobid = ?
        """, 
        (curr_post["jobid"], )
    )
    rating = cur.fetchall()

    #get all reviews from reviews table associated with the internship posting
    cur = connection.execute("SELECT fullname, content FROM reviews WHERE reviews.jobid = ?", (curr_post["jobid"],))

    reviews = cur.fetchall()

    post = {
        "title": curr_post["title"],
        "company": curr_post["cname"], 
        "subject": curr_post["jsubject"],
        "description": curr_post["jdesc"],
        "location": curr_post["loc"],
        "requirements": curr_post["jreq"],
        "link": curr_post["link"],
        "salary": curr_post["salary"],
        "jobid" : curr_post["jobid"]
    }

    return post

#get all internship postings
# @Internship.app.route("/api/posts/", methods=['GET'])
@Internship.app.route("/", methods=['GET'])
def get_internship_entries():
    connection = Internship.model.get_db()

    #get all internship postings. Get name of internship title, 
    # subject (what kind of internship), name of company, internship description, 
    # location, requirements (skills), and website link to apply (you can add more info if I missed something or 
    # remove something if you think it's not necessary)
    cur = connection.execute(
        """
        SELECT jobid, title, cname, jsubject, jdesc, loc, jreq, link, salary
        FROM jobs
        """
    )

    all_postings = cur.fetchall()
    posts = []

    for post in all_postings:
        posts.append(process_post(post, connection))

    context = {
        "posts": posts
    }
    print(context)
    return flask.render_template("index.html", **context)





def check_post(post):
    return post["title"] and post["company"] and post["jsubject"] and post["jdesc"] and post["loc"] and post["jreq"] and post["link"]


@Internship.app.route('/internship/', methods=['POST'])
def post_internship_entry():
    connection = Internship.model.get_db()


    t = str(flask.request.form['title']),
    c = str(flask.request.form['cname']),
    #s = str(flask.request.form['jsubject']),
    d = str(flask.request.form['jdesc']),
    l = str(flask.request.form['loc']),
    r = str(flask.request.form['jreq']),
    link = str(flask.request.form['link']),
    sal = int(flask.request.form['salary'])


    #insert a new internship posting from postings table in the database
    #(t, c, s, d, l, r, l, 10)
    connection.execute(
        """
        INSERT INTO jobs(title, cname, jdesc, loc, jreq, link, salary)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?)
        """, 
        ((str(t[0])), str(c[0]), str(d[0]), str(l[0]), str(r[0]), str(link[0]), int(sal))
    )
    return flask.redirect('/')

@Internship.app.route('/internship/delete/', methods=['POST'])
def delete_internship_entry():
    connection = Internship.model.get_db()

    postid = flask.request.form['postid']

    #check if the internship posting with id that matches the id in the slug exists`by selecting that posting
    connection.execute(
        """
        SELECT jobid 
        FROM jobs
        WHERE jobs.jobid = ?
        """,
        (postid, )
    )
    posting = connection.fetchone()

    if posting is None:
        flask.abort(400) 

    #delete an internship posting with id that matches the id in the slug
    connection.execute(
        """
        DELETE FROM jobs
        WHERE jobs.jobid = ?
        """,
        (postid, )
    )


@Internship.app.route("/api/posts/", methods=['POST'])
def handle_postings():
    url = flask.request.args.get('target')
    if flask.request.form['operation'] == 'create':
        post_internship_entry()
    if flask.request.form['operation'] == 'delete':
        delete_internship_entry()
    return flask.redirect(url)

@Internship.app.route('/subscription/', methods=['POST'])
def email_subscribe():
    connection = Internship.model.get_db()
    if flask.request.form['operation'] == 'create':
        comment = flask.request.form['text']
        connection.execute(
            "INSERT INTO subscribers(email, fullname) "
            "VALUES(?, ?)",
            (flask.request.form['text2'], flask.request.form['text1'])
        )

@Internship.app.before_request
def check_login():
    """Redirect to login page if not logged in."""
    if 'username' not in flask.session and flask.request.endpoint not in \
            ['static', 'show_login', 'create_account', 'accounts_post']:
        return flask.redirect(flask.url_for('show_login'))
    return None
