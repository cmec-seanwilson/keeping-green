from google.appengine.ext import ndb
# from building import Building
# from floor import Floor
from models.direction import Direction

class Bin(ndb.Model):
    # building = ndb.ReferenceKey(Building)
    # floor = ndb.ReferenceKey(Floor)
    directions = ndb.KeyProperty(Direction, repeated = True)