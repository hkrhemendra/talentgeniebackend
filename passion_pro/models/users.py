from passion_pro.models.competition import Competitions
from ..models import db
from datetime import datetime
from werkzeug.security import generate_password_hash


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), unique=False, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    dob = db.Column(db.Date, nullable=True)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean , nullable=False , default=False)
    is_teacher = db.Column(db.Boolean , nullable=False , default=False)
    confirmed_at = db.Column(db.DateTime, nullable=False,default= datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,default= datetime.utcnow)

    #teachers
    profile_picture = db.Column(db.Text)
    phone1 = db.Column(db.String(20))
    phone2 = db.Column(db.String(20))
    address = db.Column(db.Text)
    experience = db.Column(db.Text)
    qualifications = db.Column(db.Text)
    doc1 = db.Column(db.Text)
    doc2 = db.Column(db.Text)
    doc3 = db.Column(db.Text)
    doc4 = db.Column(db.Text)
    remark = db.Column(db.Text)
    rating  = db.Column(db.Integer)

    batches = db.relationship('Batches', secondary='users_batches' ,backref=db.backref('users', lazy=True))
    categories = db.relationship('Categories', secondary='users_categories' ,backref=db.backref('users', lazy=True))
    competitions = db.relationship('Competitions', secondary='users_competitions' ,backref=db.backref('users', lazy=True))

    def __init__(self,**kwargs):
        for property, value in kwargs.items():
            if property == 'password':
                value = generate_password_hash(value, method='sha256')
            setattr(self,property,value)

   