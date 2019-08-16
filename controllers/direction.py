from webapp2 import RequestHandler
from models.building import Building
from lib.jinja import jinja_env
import os

class DirectionController(RequestHandler):
    def get(self):
        # print , 'aoisdnaisndiasndi'
        building_street_number = self.request.get('building')
        floor_name = self.request.get('floor')
        building = Building.query(Building.street_number == int(building_street_number)).get()
        floor = {}
        bins = []
        for _floor in building.floors:
            _floor = _floor.get()
            if _floor.name == floor_name:
                floor = _floor
            hotspots = []
            for hotspot in _floor.hotspots:
                hotspots.append(hotspot.get())
            _floor['hotspots'] = hotspots

        if floor.bins != None:
            for _bin in floor.bins:
                _bin = _bin.get().to_dict()
                directions = []
                for direction in _bin['directions']:
                    _direction = direction.get()
                    directions.append(_direction)
                _bin['directions'] = directions
                bins.append(_bin)

        direction_template = jinja_env.get_template('templates/direction.html')
        self.response.write(direction_template.render({
            'building': building,
            'floor':  floor,
            'bins': bins,
            'http_host': os.environ['HTTP_HOST']
        }))