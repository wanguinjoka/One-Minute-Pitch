from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),unique = True, nullable = False)
    email = db.Column(db.String(255),unique = True, nullable = False)
    password = db.Column(db.String(60))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(), nullable = False, default='pic.png')
    pitchs = db.relationship('Pitch', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)
        
    # @property
    # def password(self):
    #     raise AttributeError('You cannot read the password attribute')
    # @password.setter
    # def password(self, password):
    #     self.password_hash = generate_password_hash(password)

    # def verify_password(self,password):
    #     return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"User ('{self.username}', '{self.email}','{self.profile_pic_path}')"

class Pitch(db.Model):
    __tablename__ = 'pitch'
    id = db.Column(db.Integer,primary_key = True)
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)
    content = db.Column(db.String(200),nullable = False)
    category = db.Column(db.String(20),nullable= False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable =False)
    comments = db.relationship('Comment', backref='pitch', lazy=True)

    def __repr__(self):
        return f"Pitch ('{self.content}', '{self.date_posted}','{self.category}')"

class Comment(db.Model):
	__tablename__='comment'
	id=db.Column(db.Integer,primary_key=True)
	userid=db.Column(db.Integer, db.ForeignKey('user.id'))
	pitchid=db.Column(db.Integer, db.ForeignKey('pitch.id'))
	text=db.Column(db.String(200),nullable = False)

    # def __repr__(self):
    #     return f"Comment('{self.text}','{self.userid}')"