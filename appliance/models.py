from mongoengine import connect, Document
from mongoengine import ReferenceField, StringField, DateTimeField, ListField
from mongoengine import ObjectIdField
from mongoengine.django.auth import User
from datetime import datetime
from users.models import Account

class Box(Document):
    """
    Box represents a unique WikiWall appliance
    """
    STATUS_CHOICES = (
        (u'Active', u'Active'),
        (u'New', u'Not Registered'),
        (u'Offline', u'Offline'),
        (u'Disabled', u'Disabled'),
    )

#    company = ReferenceField(Account)
#    owner = ReferenceField(User)
    name = StringField(default='New Appliance', max_length=32, required=True)
    location = StringField(max_length=100, required=False)
    status = StringField(default='Active',
                         max_length=16,
                         choices=STATUS_CHOICES,
                         required=True)
    walls = ListField(StringField())
    active_wall = StringField(required=False)
    activated = DateTimeField(default=datetime.now(), required=True)
    modified = DateTimeField(default=datetime.now(), required=True)

    def __unicode__(self):
        return self.name
