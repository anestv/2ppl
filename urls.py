import webapp2

from views import MainPage, Login, Logout, Register, Classes

#Add your urls here
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/login', Login),
    ('/logout', Logout),
    ('/register', Register),
    ('/classes', Classes)
], debug=True)
