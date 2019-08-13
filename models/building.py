from google.appengine.ext import ndb

class Building(ndb.Model):
    street_number = ndb.IntegerProperty()
    name = ndb.StringProperty()
    image = ndb.StringProperty()