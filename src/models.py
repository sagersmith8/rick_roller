import json
from google.appengine.ext import ndb


class RickRoll(ndb.Model):
    ip = ndb.StringProperty()

def get_rick_rolls_list():
    rick_rolls = RickRoll.query().fetch()
    if not rick_rolls:
        rick_rolls = []
    return rick_rolls

