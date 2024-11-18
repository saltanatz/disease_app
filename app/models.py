from . import db

class User(db.Model):
    email = db.Column(db.String(60), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    salary = db.Column(db.Integer, nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    cname = db.Column(db.String(50), nullable=False)

class Disease(db.Model):
    disease_code = db.Column(db.String(50), primary_key=True)
    pathogen = db.Column(db.String(20))
    description = db.Column(db.String(140))
    id = db.Column(db.Integer)
