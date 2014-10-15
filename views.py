import webapp2 , handler, models

#Add your views here
class MainPage(handler.Handler):
	def get(self):
		user_id = self.get_cookie('user_id')
		if user_id: 
			user = models.User.get_by_id(int(user_id))
			self.write('Hello, %s'%user.username)
		else:
			self.write('Hello you can <a href="/login">login</a>.')

class Login(handler.Handler):
	def get(self):
		self.render('login')

	def post(self):
		username = self.request.get('name')
		password = self.request.get('pass')
		self.login(username, password)
