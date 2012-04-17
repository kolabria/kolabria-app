from django.db import models
from django.forms import ModelForm, TextInput, SlugField, IntegerField

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


class UserProfile(models.Model):
    CURRENCY = (
        (u'USD', u'USD'),
        (u'CAD', u'CAD'),
    )

    user = models.OneToOneField(User)
    account = models.ForeignKey(Account)
    currency = models.CharField(max_length=3,
                                choices=CURRENCY)
    phone = models.CharField(max_length=16)
    address1 = models.CharField(max_length=30)
    address2 = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    postal_zip = models.CharField(max_length=7)
    country = models.CharField(max_length=30)
    agree_terms = models.BooleanField(default=False)


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'account', 'currency',)

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',)
