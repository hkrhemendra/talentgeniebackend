from ..models import db
from datetime import datetime

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    discription=db.Column(db.Text,nullable=False)
    remark = db.Column(db.Text)
    state = db.Column(db.String(255), nullable=False)
    ranking  = db.Column(db.Integer , nullable=False)
    image = db.Column(db.Text , nullable=False)
    video=db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False,default= datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,default= datetime.utcnow)
    courses = db.relationship('Courses', backref='category', lazy=True)
    competition = db.relationship('Competitions',backref='category',lazy=True)
    

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]
            
            setattr(self, property, value)