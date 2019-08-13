import webapp2

from controllers.building import BuildingController

app = webapp2.WSGIApplication([
    ('/', BuildingController)
], debug=True)