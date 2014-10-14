import webapp2 , handler

#Add your views here
class MainPage(handler.Handler):
	def get(self):
		self.write('Hello Wolrd!!!')
