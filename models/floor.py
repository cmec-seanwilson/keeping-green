from google.appengine.ext import ndb
from building import Building

class Floor(ndb.Model):
    number = ndb.StringProperty()
    building = ndb.ReferenceProperty(Building)