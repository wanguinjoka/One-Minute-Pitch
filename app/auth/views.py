from flask import render_template,redirect,url_for
from . import auth
from ..models import User
from .forms import SignUpForm
from .. import db

@auth.route('/signup',methods = ["GET","POST"])

def signup():
    form = SignUpForm()
    user = User(email = form.email.data, username = form.username.data,password = form.password.data)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('auth.login'))

    return render_template('auth/signup.html',signup_form = form)