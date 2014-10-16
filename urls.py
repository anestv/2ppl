import webapp2

from views import MainPage, Login, Logout, Register, Terms

#Add your urls here
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/login', Login),
    ('/logout', Logout),
    ('/register', Register),
    ('/terms', Terms)
], debug=True)
