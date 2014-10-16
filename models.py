from google.appengine.ext import db

"""DON'T MODIFY THAT MODEL"""
class User(db.Model):
	username = db.StringProperty(required=True)
	name = db.StringProperty(required=True)
	password = db.StringProperty(required=True)
	email = db.StringProperty(required=True)
	usertype = db.StringProperty(required=True)

#Add your models here