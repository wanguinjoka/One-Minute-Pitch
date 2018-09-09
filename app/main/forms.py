from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Length,Email,EqualTo
from wtforms import ValidationError
from ..models import User, Pitch


class PitchForm(FlaskForm):
    category = StringField('Category', validators=[Required()])
    content= TextAreaField('Content', validators=[Required()])
    submit = SubmitField('Pitch')