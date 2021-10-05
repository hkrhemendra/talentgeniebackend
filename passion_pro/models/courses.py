import re
from ..models import db
from datetime import datetime

class Courses(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(80), unique=False, nullable=False)
    discription=db.Column(db.Text,nullable=False)
    prerequisites=db.Column(db.Text,nullable=False)
    category_fk = db.Column(db.Integer, db.ForeignKey('categories.id'),nullable=False)
    minage=db.Column(db.Integer, nullable=False)
    maxage=db.Column(db.Integer, nullable=False)
    coursetype=db.Column(db.String(30), nullable=False)
    rating  = db.Column(db.Integer)
    remark = db.Column(db.Text)
    level = db.Column(db.String(20),nullable=False)
    broucher=db.Column(db.Text, nullable=False)
    thumbnail_image=db.Column(db.Text, nullable=False)
    video=db.Column(db.Text, nullable=False)
    course_code = db.Column(db.String(80), unique=True, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False , default= datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,default= datetime.utcnow)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]
            
            setattr(self, property, value)
