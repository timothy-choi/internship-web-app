import flask 
import Internship

#Here's my implementation of the Flask routes for the reviews component of the postings. 
#Since we said that we would have reviews for each posting, I decided to add routes for this part as well

@Internship.app.route('/review/add/<postid_slug>/', methods=['POST'])
def add_review(postid_slug):
    connection = Internship.model.get_db()
    logname = flask.session.get('username', None)
    if not flask.request.form['review']:
        flask.abort(400)
    content = flask.request.form['review']
    #add review to the Reviews table in database for a specific internship posting.
    connection.execute(
        """
        INSERT INTO reviews(jobid, content, user)
        VALUES (?, ?, ?)
        """,
        (postid_slug, content, logname)
    )
    return flask.redirect('/reviews/' + postid_slug + '/')


@Internship.app.route('/review/delete/', methods=['POST'])
def delete_review():
    connection = Internship.model.get_db()
    review_id = flask.request.form['reviewid']
    #jod_id = flask.request.form['jobid'] 
    #review = connection.fetchone()
    #if review.length == 0:
        #flask.abort(400)
    target = flask.request.args["target"]
    #delete review from the Reviews table in database with same id as reviewid.
    connection.execute(
        """
        DELETE FROM reviews
        WHERE reviewid = ?
        """,
        (review_id, )
    )
    return flask.redirect(target)


@Internship.app.route("/reviews/<job_id>/", methods=['GET'])
def get_ratings_and_reviews(job_id):
    connection = Internship.model.get_db()
    cur = connection.execute(
        """
        SELECT jobid, reviewid, fullname, content, user
        FROM reviews
        WHERE jobid == ?
        """,
        (job_id, )
    )
    items = cur.fetchall()
    
    cur1 = connection.execute(
        """
        SELECT AVG(rating) as rate
        FROM ratings
        WHERE jobid == ?
        """,
        (job_id, )
    )
    cur2 = connection.execute(
        """
        SELECT ratingid 
        FROM ratings
        WHERE jobid == ?
        """,
        (job_id, )
    )
    rt = cur1.fetchone()["rate"]
    r2 = cur2.fetchone()["ratingid"]
    context = {"job": items, "rating" : rt, "jid" : job_id, "rid" : r2}

    return flask.render_template("job.html", **context)

