from google.appengine.ext import ndb
from models.bin import Bin
from models.hotspot import HotSpot

class Floor(ndb.Model):
    name = ndb.StringProperty()
    bins = ndb.KeyProperty(Bin, repeated = True)
    hotspots = ndb.KeyProperty(HotSpot, repeated = True)