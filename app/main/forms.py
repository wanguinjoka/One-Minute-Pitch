from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,PasswordField,SubmitField,BooleanField,SelectField
from wtforms.validators import Required,Length,Email,EqualTo
from wtforms import ValidationError
from ..models import Comment, User, Pitch


class PitchForm(FlaskForm):
    category_id = SelectField('Select Category', choices = [('1','Inspire Someone'),('2','Get Hired'),('3','Get the Gal')])
    content= TextAreaField('Content', validators=[Required()])
    submit = SubmitField('Pitch')

class CommentForm(FlaskForm):
    text = TextAreaField('Content')
    submit = SubmitField('Comment')