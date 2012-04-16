from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Account(models.Model):
    """
    Corporate Account model in django to represent Company objects
    """
    STATUS_CHOICES = (
        (u'Active', u'Active'),
        (u'Inactive', u'Inactive'),
    )

    name = models.CharField(max_length=30)
    domain = models.CharField(max_length=30)
    owner = models.ForeignKey(User)
    status = models.CharField(default='Active', 
                         max_length=8, 
                         choices=STATUS_CHOICES,
                         )
    created = models.DateTimeField(default=datetime.now())
    modified = models.DateTimeField(default=datetime.now())

    def __unicode__(self):
        """
        Returns the Wall Name as unicode description for admin and shell
        """
        return self.name
