import webapp2
import os

from controllers.building import BuildingController

app = webapp2.WSGIApplication([
    ('/', BuildingController)
], debug=True)