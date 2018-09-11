from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .. import db
from ..models import User, Pitch, Comment
from flask_login import login_required,current_user
from .forms import PitchForm, CommentForm

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    pitchs =Pitch.query.all()
    comments = Comment.query.all()
    return render_template('index.html', pitchs = pitchs, comments = comments)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    profile_pic_path = url_for('static', filename='profilepic/'+ user.profile_pic_path)

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, profile_pic_path=profile_pic_path)

@main.route('/pitch/new', methods =['GET','POST'])
@login_required
def new_pitch():
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        pitch = Pitch(category_id=pitch_form.category_id.data, content=pitch_form.content.data, author=current_user)
        db.session.add(pitch)
        db.session.commit()
        flash('Your pitch has been created!', 'success')
        return redirect(url_for('main.index'))

    
    return render_template("create_pitch.html", pitch_form = pitch_form)

@main.route('/comment', methods =['GET','POST'])
@login_required
def new_comment():
    pitch_id = Pitch.query.filter_by(id= 'pitch_id').filter()
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = Comment(text=comment_form.text.data, author=current_user)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been updated', 'success')
        return redirect(url_for('main.index'))

    return render_template("comment.html", comment_form = comment_form, pitch_id = pitch_id)

    

