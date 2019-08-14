import webapp2

from controllers.building import BuildingController
from controllers.floor import FloorController
from controllers.direction import DirectionController
from models.seeder import seed
from lib.jinja import jinja_env
 
class SeedDatabase(webapp2.RequestHandler):
    def get(self):
        seed()
        self.response.write('Database Successfully Seeded')

app = webapp2.WSGIApplication([
    ('/', BuildingController),
    ('/floors', FloorController),
    ('/directions',  DirectionController),
    ('/seed', SeedDatabase)
], debug=True)