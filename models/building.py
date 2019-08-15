from google.appengine.ext import ndb
from models.floor import Floor

class Building(ndb.Model):
    street_number = ndb.IntegerProperty()
    name = ndb.StringProperty()
    image = ndb.StringProperty()
    floors = ndb.KeyProperty(Floor, repeated = True)