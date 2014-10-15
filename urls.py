import webapp2

from views import MainPage, Login, Logout

#Add your urls here
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/login', Login),
    ('/logout', Logout)
], debug=True)
