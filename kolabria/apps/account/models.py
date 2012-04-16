from django.db import models
from django.forms import ModelForm
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
    slug = models.SlugField(max_length=20)
    box_count = models.IntegerField()
    owner = models.ForeignKey(User, editable=False)
    status = models.CharField(default='Active', 
                              max_length=8, 
                              choices=STATUS_CHOICES,
                              editable=False)
    created = models.DateTimeField(default=datetime.now(),
                                   editable=False)
    modified = models.DateTimeField(default=datetime.now(),
                                    editable=False)

    def __unicode__(self):
        """
        Returns the Wall Name as unicode description for admin and shell
        """
        return self.name


class AccountForm(ModelForm):
    class Meta:
        model = Account
