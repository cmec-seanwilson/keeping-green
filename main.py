import webapp2

from controllers.building import BuildingController
from lib.jinja import jinja_env
import webapp2

floors = [
    { 'name': 'Sub', 'building': 1653 },
    { 'name': 'Main', 'building': 1653 },
    { 'name':  '2nd', 'building': 1653 },
    { 'name': '3rd', 'building': 1653 },
    { 'name': '4th', 'building': 1653 },
    { 'name': '5th', 'building': 1653 }
]

buildings = [
    { 'street_number': 1653, 'name': 'AB-1' }
]

bins = [
    { 'building': 1653, 'floor': 'Sub', 'id': 1 }
]

directions = [
    { 'bin': 1, 'step': 1, 'message': 'foo bar' }
]

class Buildings(webapp2.RequestHandler):
    def get(self):
        buildings_template = jinja_env.get_template('templates/index.html')
        buildings_linked = []
        for building in buildings:
            building['link'] = '/floors?building=' + str(building['street_number'])
            buildings_linked.append(building)
        self.response.write(buildings_template.render({
            'buildings': buildings_linked
        }))

class Floors(webapp2.RequestHandler):
    def get(self):
        building_street_number = self.request.get('building')
        building = {}
        building_floors = []

        for _building in buildings:
            if str(_building['street_number']) == building_street_number:
                building = _building

        for floor in floors:
            if str(floor['building']) == building_street_number:
                floor['link'] = '/directions?building=%s&floor=%s'%(floor['building'], floor['name'])
                building_floors.append(floor)
        
        floors_template = jinja_env.get_template('templates/floors.html')
        self.response.write(floors_template.render({
            'building': building,
            'floors': building_floors
        }))

app = webapp2.WSGIApplication([
    ('/', Buildings),
    ('/floors', Floors)
], debug=True)