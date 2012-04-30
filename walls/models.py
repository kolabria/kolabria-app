from django.core.exceptions import ObjectDoesNotExist, ValidationError

from django.db import models
from django.forms import ModelForm, TextInput, SlugField, IntegerField

from mongoengine import connect, Document
from mongoengine import ReferenceField, StringField, DateTimeField
from mongoengine import EmailField, ListField, ObjectIdField

from django.contrib.auth.models import User
#from mongoengine.django.auth import User
from users.models import Account
from appliance.models import Box
from datetime import datetime
from django import forms


class Wall(models.Model):
    """
    Wall model in SQL to represent Wall objects
    """
    owner = models.ForeignKey(User, editable=False)
    name = models.CharField('Wall Name', max_length=30)
    description = models.CharField('Description', max_length=256)

    def __unicode__(self):
        """
        Returns the Wall Name as unicode description for admin and shell
        """
        return self.name


class WallForm(ModelForm):
    class Meta:
        model = Wall

"""
class Wall(Document):
   STATUS_CHOICES = (
        (u'Active', u'Active'),
        (u'Private', u'Private'),
        (u'Inactive', u'Inactive'),
    )        
#    company = ReferenceField(Account)
    owner = ReferenceField(User)
    name = StringField(max_length=32, required=True)
    description = StringField(max_length=256, required=False)
    status = StringField(default='Active', 
                         max_length=8, 
                         choices=STATUS_CHOICES,
                         required=True)
    created = DateTimeField(default=datetime.now(), required=False)
    modified = DateTimeField(default=datetime.now(), required=True)
    published = ListField(StringField())
    sharing = ListField(EmailField())
    viewing = ListField(EmailField())


    def __unicode__(self):
        return self.name

    def clean(self):
        # check appliance_id is valid before appending id to Wall.published 
        for id in published:
            if not Box.objects.get(id=id):
                raise ValidationError('Invalid Appliance_id: %s' % id)
"""
