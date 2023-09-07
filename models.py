from sqlalchemy import SQLAlchemy
from . import db
db = SQLAlchemy()

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(200))
