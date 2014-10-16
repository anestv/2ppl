import webapp2 , handler, models

#Add your views here
class MainPage(handler.Handler):
	def get(self):
		user_id = self.get_cookie('user_id')
		if user_id: 
			user = models.User.get_by_id(int(user_id))
			self.write('Hello, %s'%user.username)
			self.write('<br><a href="/logout">logout</a>')
		else:
			self.render('login')

class Login(handler.Handler):
	def get(self):
		user_id = self.get_cookie('user_id')
		if user_id:
			self.redirect('/')
		else:
			self.render('login')

	def post(self):
		username = self.request.get('name')
		password = self.request.get('pass')
		self.login(username, password)


class Logout(handler.Handler):
	def get(self):
		self.logout()


class Register(handler.Handler):
	def get(self):
		self.render('register')

	def post(self):
		username = self.request.get('username')
		name = self.request.get('fullname')
		email = self.request.get('email')
		password = self.request.get('password')
		verify = self.request.get('verify')
		type_of_user = self.request.get('type')

		if handler.valid_register(username, password, verify, email):
			self.register(username, name, password, email, type_of_user)
		else:
			error = 'The data order is not valid'
			self.render('register', username=username, name=name, email=email, error=error)


class Terms(handler.Handler):
	def get(self):
		self.render('terms')