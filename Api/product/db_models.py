from Api import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    Currency = db.Column(db.String(10), nullable=False)
    Description = db.Column(db.String(250), nullable=True)
