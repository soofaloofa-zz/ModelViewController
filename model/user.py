from google.appengine.ext import ndb


class User(ndb.Model):

    name = ndb.StringProperty()

    @classmethod
    def get_or_create(cls, name):
        if not name:
            return None

        user = ndb.Key('User', name).get()
        if not user:
            user = User(name=name, id=name)
            user.put()
        return user
