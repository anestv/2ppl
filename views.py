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


class Profile(handler.Handler):
	def get(self):
		username = '1'