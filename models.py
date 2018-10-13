from app import db

class Trades(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date)
    place = db.Column(db.String(30))
    food = db.Column(db.String(1000))
