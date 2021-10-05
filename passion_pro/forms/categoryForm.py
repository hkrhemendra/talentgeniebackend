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
class addCategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)]) 
    discription = TextAreaField('Discription',validators=[DataRequired()])
    remark = TextField('Remark',validators=[DataRequired()])
    state = SelectField('State',validators=[DataRequired()],choices=["Active","InActive"],coerce=str)
    ranking = SelectField('Rank' ,coerce=int,choices=[1,2,3,4,5,6,7,8,9,10],validators=[DataRequired()])
    image = FileField('Image Realeted To Category',validators=[FileRequired()])
    video = FileField('Short Video')
   


# Category Name
# Short Description of Category
# Remarks
# Active state - option field
# Ranking order - option field

# Image
# Video - optional field