from flask import Flask
import flask.ext.sqlalchemy


app = Flask(__name__)
app.config.from_object('config')
db = flask.ext.sqlalchemy.SQLAlchemy(app)

from app import database, graph, sabre, views