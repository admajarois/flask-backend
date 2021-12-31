from datetime import timezone
from . import db


class Barang(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    id_category = db.Column(db.Integer, db.ForeignKey('category.id'))
    stock = db.Column(db.Integer)
    image = db.Column(db.String(255))
    date = db.Column(db.DateTime(timezone=True))
    category = db.relationship('Category')


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
