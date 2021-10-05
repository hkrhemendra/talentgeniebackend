from ..models import db

users_categories = db.Table('users_categories',
    db.Column('user_fk', db.Integer, db.ForeignKey('users.id')),
    db.Column('category_fk', db.Integer, db.ForeignKey('categories.id'))
)