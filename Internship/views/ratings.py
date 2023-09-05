import flask 
import Internship

#Here's my implementation of the Flask routes for the rating component of the postings. 
#Since we said that we would have ratings for each posting, I decided to add routes for this part as well

@Internship.app.route('/rating/create/<postid_slug>/', methods=['POST'])
def add_rating(postid_slug):
    connection = Internship.model.get_db()
    logname = flask.session.get('username', None)
    rating = flask.request.form['rate']
    #insert rating to ratings table database for a specific internship posting
    connection.execute(
        """
        INSERT INTO ratings(jobid, rating, user)
        VALUES (?, ?, ?)
        """,
        (postid_slug, int(rating), logname)
    )
    return flask.redirect('/reviews/' + postid_slug + '/')

@Internship.app.route('/rating/delete/', methods=['POST'])
def delete_rating():
    connection = Internship.model.get_db()
    ratingid = flask.request.form['ratingid']
    #check if the rating in ratings table for that specific internship posting exists in the database
    target = flask.request.args["target"]
    logname = flask.session.get('username', None)
    #delete rating from the ratings table in the database for a specific internship posting
    connection.execute(
        """
        DELETE FROM ratings
        WHERE user = ?
        """,
        (logname,)
    )
    return flask.redirect(target)

