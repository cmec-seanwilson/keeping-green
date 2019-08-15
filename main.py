import webapp2

from controllers.building import BuildingController
from controllers.floor import FloorController
from controllers.direction import DirectionController
from models.seeder import seed
from lib.jinja import jinja_env
 
class SeedDatabase(webapp2.RequestHandler):
    def get(self):
        password = self.request.get('password')
        if password == 'cssi-x-19-keeping-green-shiki':
            seed()
            self.response.write('Database Successfully Seeded')
        else:
            self.response.write('Incorrect password.')
app = webapp2.WSGIApplication([
    ('/', BuildingController),
    ('/floors', FloorController),
    ('/directions',  DirectionController),
    ('/seed', SeedDatabase)
], debug=True)