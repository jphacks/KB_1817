from sqlalchemy.orm import synonym
from werkzeug import check_password_hash, generate_password_hash
from charin import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), default='', nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    _password = db.Column('password', db.String(100), nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    to_whom_id = db.Column(db.Integer, nullable=False)
    from_whom_id = db.Column(db.Integer, nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
def init():
    db.create_all()