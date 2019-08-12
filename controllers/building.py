from webapp2 import RequestHandler
from lib.jinja import jinja_env

class BuildingController(RequestHandler):
    def get(self):
        # fetch buildings from database
        buildings_template = jinja_env.get_template('templates/index.html')
        self.response.write(buildings_template.render())