from google.appengine.ext import ndb
from building import Building
from floor import Floor

class Direction(ndb.Model):
    building = ndb.ReferenceProperty(Building)
    floor = ndb.ReferenceProperty(Floor)
    step = ndb.IntegerProperty()
    message = ndb.TextProperty()
    icon = ndb.StringProperty()