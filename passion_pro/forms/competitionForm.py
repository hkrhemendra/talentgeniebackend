import datetime
from typing import Pattern
from flask_wtf import FlaskForm
from sqlalchemy.sql.sqltypes import Integer, String
from werkzeug.datastructures import Accept, MultiDict
from wtforms import SelectField,StringField,TextAreaField,IntegerField
from wtforms import validators
from wtforms.fields.core import BooleanField, DateTimeField, IntegerField
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import InputRequired, Email,DataRequired,Length,ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed



class addcompetitionForm(FlaskForm):
    def validate_time_field(form, field):
        if field.data < form.competition_start_time.data:
            raise ValidationError("End Time must not be earlier than start Time.")
    def validate_date_field(form, field):
         if field.data < form.registration_start.data:
             raise ValidationError("End date must not be earlier than start date.")
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=20)])
    competition_start_time  = DateTimeLocalField('Start Time', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    competition_end_time    = DateTimeLocalField('End Time',  format='%Y-%m-%dT%H:%M',  validators=[DataRequired(),validate_time_field])
    registration_start=DateTimeLocalField('Registration Start Date',format='%Y-%m-%dT%H:%M',validators=[DataRequired()])
    registration_end=DateTimeLocalField('Registration End Date',format='%Y-%m-%dT%H:%M',validators=[DataRequired(),validate_date_field])
    category_fk = SelectField('Category' ,validators=[DataRequired()],coerce=int)
    image = FileField('Image',validators=[FileRequired()])
    minage= IntegerField('Min Age',validators=[DataRequired()])
    maxage = IntegerField('Max Age',validators=[DataRequired()])
    gender = SelectField('Gender',coerce=str,choices=["None","Male","Female","Other"])
    remark = StringField('Remark', validators=[DataRequired()])
    discription = TextAreaField('Discription',validators=[DataRequired()])

   
    