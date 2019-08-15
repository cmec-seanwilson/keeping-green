from google.appengine.ext import ndb

class Direction(ndb.Model):
    step = ndb.IntegerProperty()
    message = ndb.TextProperty()
    image = ndb.StringProperty()