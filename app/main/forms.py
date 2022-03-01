from flask_wtf import FlaskForm 
from wtforms import StringField,TextAreaField,SubmitField

class ReviewForm(FlaskForm):

    submit = SubmitField('SEarch')