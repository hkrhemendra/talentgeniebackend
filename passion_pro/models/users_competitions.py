from ..models import db

users_competitions = db.Table('users_competitions',
    db.Column('user_fk', db.Integer, db.ForeignKey('users.id')),
    db.Column('competition_fk', db.Integer, db.ForeignKey('competitions.id')),
    db.Column('work_submission',db.Text),
    db.Column('position',db.Integer),
    db.Column('submission_on',db.Date),
    db.Column('participated_on',db.Date)
)

# class Users_competitions(db.Model):
    
#     user_fk = db.Column(db.ForeignKey('users.id'), primary_key=True)
#     competition_fk = Column(ForeignKey('right.id'), primary_key=True)
#     extra_data = Column(String(50))

#     child = relationship("Child", backref="parent_associations")
#     parent = relationship("Parent", backref="child_associations")