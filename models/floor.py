from google.appengine.ext import ndb
from models.bin import Bin

class Floor(ndb.Model):
    name = ndb.StringProperty()
    bins = ndb.KeyProperty(Bin, repeated = True)