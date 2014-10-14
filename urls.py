import webapp2

from views import MainPage

#Add your urls here
application = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
