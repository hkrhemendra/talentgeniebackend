from ..models import db
from datetime import datetime

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _from = db.Column(db.String(120), nullable=False)
    to = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.Text)
    body = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False,default= datetime.utcnow)