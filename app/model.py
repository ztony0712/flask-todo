# this is the file for data table init

from app import db, app


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    complete = db.Column(db.Boolean)
    date = db.Column(db.Date)
    code = db.Column(db.String(50))
    dcp = db.Column(db.String(500))
    total = db.Column(db.Integer)
    step = db.Column(db.Integer)
