import datetime
from typing import Pattern
from flask_wtf import FlaskForm
from sqlalchemy.sql.sqltypes import Integer, String
from werkzeug.datastructures import Accept, MultiDict
from wtforms import TextField, PasswordField ,SelectField,StringField,SubmitField,SelectMultipleField,TextAreaField,IntegerField
from wtforms import validators
from wtforms.fields.core import BooleanField, IntegerField
from wtforms.validators import InputRequired, Email,DataRequired,Length
from flask_wtf.file import FileField, FileRequired, FileAllowed
class addCourseForm(FlaskForm):
    course_name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)]) 
    discription = TextAreaField('Discription',validators=[DataRequired()])
    prerequisites = TextAreaField('Prerequisites',validators=[DataRequired()])
    category_fk = SelectField('Category' ,validators=[DataRequired()],coerce=int)
    minage= IntegerField('Min Age',validators=[DataRequired()])
    maxage = IntegerField('Max Age',validators=[DataRequired()])
    coursetype = SelectField('Course Type',validators=[DataRequired()],choices=["One Time","Recurring"],coerce=str)
    rating = SelectField('Rate' ,coerce=int,choices=[1,2,3,4,5,6,7,8,9,10])
    remark = TextField('Remark')
    level = SelectField('Course Level',validators=[DataRequired()],choices=["Beginner","Intermediate","Advanced"],coerce=str)
    broucher = FileField('Broucher',validators=[FileRequired()])
    thumbnail_image = FileField('ThumbNail Image',validators=[FileRequired()])
    video = FileField('Short Video',validators=[FileRequired()])
    
