import flask 
import Internship


@Internship.app.route("/archive/", methods=['GET'])
def get_archive():
    connection = Internship.model.get_db()
    cur = connection.execute(
        """
        SELECT jobid, title, cname, salary, postdate, closedate
        FROM archive
        ORDER BY closedate DESC
        """
    )
    items = cur.fetchall()
    #for item in items:
        #item['postdate'] = arrow.get(item['postdate']).humanize()
        #item['closedate'] = arrow.get(item['closedate']).humanize()
    for item in items:
        item['postdate'] = item['postdate'][:10]
        item['closedate'] = item['closedate'][:10]
    context = {"archive": items}

    return flask.render_template("archive.html", **context)

@Internship.app.route("/archive/", methods=['POST'])
def post_archive():
    connection = Internship.model.get_db()
    new_posting = {
        "title": flask.request.form['title'],
        "company": flask.request.form['cname'],
        "salary": flask.request.form['salary'],
        "postdate": flask.request.form['postdate'],
        "closedate": flask.request.form['closedate']
    }

    cur = connection.execute(
        """
        INSERT INTO archive (title, cname, salary, postdate, closedate)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (new_posting["title"], new_posting["company"], new_posting["salary"], new_posting["postdate"], new_posting["closedate"])
    )