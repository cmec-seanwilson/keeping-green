from webapp2 import RequestHandler
from lib.jinja import jinja_env

from models.building import Building
# from models.floor 

class FloorController(RequestHandler):
    def get(self):
        # print 'hello world'
        building_street_number = self.request.get('building')
        building = Building.query(Building.street_number == int(building_street_number)).get()
        floors = []
        for floor in building.floors:
            floors.append(floor.get())
        #  '/directions?building=%s&floor=%s'%(floor['building'], floor['name'])
        floors_template = jinja_env.get_template('templates/floors.html')
        self.response.write(floors_template.render({
            'building': building,
            'floors': floors
        }))
    