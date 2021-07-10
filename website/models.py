from . import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    semester = db.Column(db.Integer)
    supples = db.relationship('Supple')

class Supple(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    subject = db.Column(db.String(150)) 
    semester = db.Column(db.String)
    modules_covered = db.Column(db.Integer)
    modules_left =  db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))



