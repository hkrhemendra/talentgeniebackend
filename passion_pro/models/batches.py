from ..models import db
from datetime import datetime

class Batches(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    batch_size = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer , nullable=False)
    batch_start = db.Column(db.Date , nullable=False)
    batch_end = db.Column(db.Date , nullable=False)
    time_from =  db.Column(db.Time, nullable=False)
    time_to =  db.Column(db.Time, nullable=False)
    rating  = db.Column(db.Integer)
    weekDays =  db.Column(db.String(150), nullable=False)
    is_active = db.Column(db.Boolean , nullable=False ,default= False)
    remark = db.Column(db.Text)
    discription=db.Column(db.Text)
    discount =  db.Column(db.Integer)
    confirmed_at = db.Column(db.DateTime, default= datetime.utcnow)
    updated_at = db.Column(db.DateTime, default= datetime.utcnow)
    link = db.Column(db.Text)
    meetingid = db.Column(db.Text)
    meetingpass = db.Column(db.Text)
    courses = db.relationship('Courses', secondary='batches_courses' ,backref=db.backref('batches', lazy=True))

    def __init__(self,**kwargs):
        for property, value in kwargs.items():
            setattr(self,property,value)
    