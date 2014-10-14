"""DON'T MODIFY THIS FILE"""

import webapp2, jinja2, os, hashlib, re, random, string, hashlib, models

from models import User

__name__ = 'handler'
JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader('templates') , autoescape = True)
SECRET = "SECRET"

#Hashing
def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return "%s,%s"%(h,salt)

def is_valid_pw(name, pw, h):
	salt = h.split(',')[1]
	if make_pw_hash(name, pw, salt) == h:
		return True
	else:
		return False

def make_cookie_hash(value):
	value = str(value)
	if value == "":
		return ""
	else:
    		h = hashlib.sha256(value + SECRET).hexdigest()
    		return "%s|%s"%(value,h)

def valid_cookie(hashed_value):
	if hashed_value:
		value = hashed_value.split('|')[0]
		if make_cookie_hash(value) == hashed_value:
			return value


#Request handler
class Handler(webapp2.RequestHandler):
	def write(self , *a , **kw):
		self.response.write(*a , **kw)

	def render(self , htmlFile , **params):
		page = JINJA_ENV.get_template(htmlFile+'.html')
		self.write(page.render(params))

	def set_cookie(self, name, value, path='/'):
		hashed_cookie =	make_cookie_hash(value)
		cookie_val = "%s=%s;Path=%s" % (name, hashed_cookie, path)
		self.response.headers.add_header('Set-Cookie', cookie_val)

	def get_cookie(self, cookie_name):
		cookie_val = self.request.cookies.get(cookie_name)
		return valid_cookie(cookie_val)

	def login(self, username, password):
		user = User.all().filter('username =', username).get()
		if user == None:
			error = 'The username doesn\'t exist'
			self.render('login', error=error, username=username, password=password)
		elif user.username == username and is_valid_pw(username, password, user.password):
			self.set_cookie('user_id', user.key().id())
			self.redirect('/')
		else:
			error = 'The password is not corect.'
			self.render('login', error=error, username=username, password=password)

	def logout(self):
		self.set_cookie('user_id', "")

	def register(self, username, password, email):
		pw = make_pw_hash(username, password)
		user = User(username=username, password=pw, email=email)
		user.put()
		user_id = user.key().id()
		self.set_cookie('user_id', user_id)
		self.redirect('/')

	def initialize(self, *a, **kw):
        	webapp2.RequestHandler.initialize(self, *a, **kw)
        	user_id = self.get_cookie('user_id')
        	if user_id:
        		user_id = int(user_id)
        		self.user = user_id and User.get_by_id(user_id)
        	else:
        		self.user = None


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PW_RE = re.compile(r"^.{3,20}$")
MAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_user(username):
	if username:
		return USER_RE.match(username)

def valid_pw(password):
	if password:
		return PW_RE.match(password)

def valid_mail(email):
	if email:
		return MAIL_RE.match(email)

def valid(username, password, email=None):
	user = valid_user(username)
	pw = valid_pw(password)
	if user and pw:
		if email and valid_mail(email):
			return True
		elif email and not valid_mail(email):
			return None
		else:
			return True
