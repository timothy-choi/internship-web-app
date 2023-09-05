import flask

app = flask.Flask(__name__)

app.config.from_object('Internship.config')


app.config.from_envvar('INTERSHIP_SETTINGS', silent=True)
 

import Internship.model
import Internship.views