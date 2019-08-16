from google.appengine.ext import ndb

class HotSpot(ndb.Model):
  pitch = ndb.IntegerProperty()
  yaw = ndb.IntegerProperty()
  text = ndb.StringProperty()