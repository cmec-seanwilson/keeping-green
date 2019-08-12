import webapp2
import jinja
import os

import controllers

app = webapp2.WSGIApplication([
    ('/', controllers.building.BuildingController)
], debug=True)