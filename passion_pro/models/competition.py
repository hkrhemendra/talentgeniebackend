from ..models import db
from datetime import datetime

class Competitions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    competition_start_time =  db.Column(db.DateTime, nullable=False)
    competition_end_time =  db.Column(db.DateTime, nullable=False)
    registration_start = db.Column(db.DateTime , nullable=False)
    registration_end = db.Column(db.DateTime , nullable=False)
    category_fk = db.Column(db.Integer, db.ForeignKey('categories.id'),nullable=False)
    minage=db.Column(db.Integer, nullable=False)
    maxage=db.Column(db.Integer, nullable=False)
    gender=db.Column(db.String(10))
    remark=db.Column(db.String(50),nullable=False)
    discription=db.Column(db.Text,nullable=False)
    requirements=db.Column(db.Text)
    rating  = db.Column(db.Integer)
    image=db.Column(db.Text, nullable=False)
    code = db.Column(db.String(80), unique=True, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False,default= datetime.now)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]
            
            setattr(self, property, value)


    