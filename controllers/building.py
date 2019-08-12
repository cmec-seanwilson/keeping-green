from webapp2 import RequestHandler
from lib.jinja import jinja_env

from models.building import Building

class BuildingController(RequestHandler):
    def get(self):
        buildings = Building.query().fetch()
        # fetch buildings from database
        template_ctx = {
            "buildings": buildings
        }
        buildings_template = jinja_env.get_template('templates/index.html')
        self.response.write(buildings_template.render(template_ctx))