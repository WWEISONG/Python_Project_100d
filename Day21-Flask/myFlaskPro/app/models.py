from app import db
from datetime import datetime

class User(db.Model):
	# use Column to build attribute, designate priamry key or unique
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	# python magic method
	# tell python how to print objects of this class
	def __repr__(self):
		return f'<User {self.username}>'

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return f'<Post {self.body}>'