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
    { 'name': '5th', 'building': 1653 },
    { 'name': 'Library Main', 'building': 1650 },
    { 'name': 'Library Sub', 'building': 1650 }
]

buildings = [
    { 'street_number': 1653, 'name': 'AB-1' },
    { 'street_number': 1650, 'name': 'Bedford' }
]

bins = [
    { 'building': 1650, 'floor': 'Library Main', 'id': 1 },
    { 'building': 1650, 'floor': 'Library Sub', 'id': 2 }
]

directions = [
    { 'bin': 1, 'step': 1, 'message': 'Under the stairs by the <strong>Printing Room</strong> is recycling and trash cans' },
    { 'bin': 2, 'step': 1, 'message': 'Towards the elevator opposite of the <strong>Printing Room</strong>' }
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

class Directions(webapp2.RequestHandler):
    def get(self):
        building_street_number = self.request.get('building')
        building_floor = self.request.get('floor')

        building = [b for b in buildings if str(b['street_number']) == building_street_number][0]
        floor = [f for f in floors if str(f['building']) == building_street_number and f['name'] == building_floor][0]
        floor_bins = []

        # print building, floor, 'floor, building'

        for bin in bins:
            if str(bin['building']) == building_street_number and bin['floor'] == building_floor:
                bin['directions'] = []
                for direction in directions:
                    if direction['bin'] == bin['id']:
                        bin['directions'].append(direction)
                bin['directions'] = sorted(bin['directions'], lambda d: d['step'])
                floor_bins.append(bin)
        
        direction_template = jinja_env.get_template('templates/direction.html')
        self.response.write(direction_template.render({
            'building': building,
            'floor':  floor,
            'bins': floor_bins
        }))


app = webapp2.WSGIApplication([
    ('/', Buildings),
    ('/floors', Floors),
    ('/directions',  Directions)
], debug=True)