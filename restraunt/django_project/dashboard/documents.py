'''
    MongoEngine Documents
'''
from mongoengine import connect, Document, fields
from django.conf import settings
connect(host=settings.MONGODB_CONNECT_STRING)


class Actions(Document):
    '''
        Restraunt Actions
    '''
    dish = fields.StringField()
    station = fields.StringField()
    action = fields.StringField()
    duration = fields.FloatField()
    startTime = fields.DateTimeField()
