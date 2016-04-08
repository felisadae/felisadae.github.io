# DATABASE.PY
# Handles logic related to account storage in the database.

from app import db


class Flight(db.Model):
    """
    Model representing a flight and its duration.
    Represented as LAX|JFK = 10 (assuming bidirectionality)
    """
    flight = db.Column(db.String(10), primary_key=True, unique=True)
    duration = db.Column(db.Integer)

    def __init__(self, origin, destination, duration):
        self.flight = origin + "|" + destination
        self.duration = duration

    def __repr__(self):
        return '<Flight %r>' % self.net_id