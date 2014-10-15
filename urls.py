import webapp2

from views import MainPage, Login

#Add your urls here
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/login', Login)
], debug=True)
