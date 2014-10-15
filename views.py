import webapp2 , handler

#Add your views here
class MainPage(handler.Handler):
	def get(self):
		self.write('Hello Wolrd!!!')

class Login(handler.Handler):
	def get(self):
		self.render('login')

	def post(self):
		username = self.request.get('name')
		password = self.request.get('pass')
		self.login(username, password)
