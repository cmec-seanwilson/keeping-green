from google.appengine.ext import ndb
from building import Building

class Floor(ndb.Model):
    name = ndb.StringProperty()
    building = ndb.ReferenceProperty(Building)