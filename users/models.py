# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm, TextInput, SlugField, IntegerField

from django.contrib.auth.models import User
from datetime import datetime


class Account(models.Model):
    """
    Corporate Account model in django to represent Company objects
    """
#    STATUS_CHOICES = (
#        (u'Active', u'Active'),
#        (u'Inactive', u'Inactive'),
#    )
    company = models.CharField("Company Name", max_length=30)
    subdomain = models.SlugField("Company Subdomain", max_length=30)
    owner = models.ForeignKey(User, blank=True, null=True, editable=False)
#    status = models.CharField(default='Active', 
#                              max_length=8, 
#                              choices=STATUS_CHOICES,
#                              editable=False)
#    created = models.DateTimeField(default=datetime.now(),
#                                   editable=False)
#    modified = models.DateTimeField(default=datetime.now(),
#                                    editable=False)

    def __unicode__(self):
        """
        Returns the Wall Name as unicode description for admin and shell
        """
        return self.company

class AccountForm(ModelForm):
    class Meta:
        model = Account

class Profile(models.Model):
    """
    User profile model 
    web_site, about, city, user
    """
    admin = User.objects.filter(username='admin')[0]
    user = models.OneToOneField(User, default=admin, blank=True, null=True, verbose_name='Profile')
    account = models.ForeignKey(Account, blank=True, null=True, editable=False)
    web_site = models.URLField('Website', max_length=255, blank=True, null=True)
    about = models.TextField('About', max_length=500, blank= True, null=True)
    city = models.CharField(verbose_name='City', blank=True, null=True,
                            max_length=30)

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ['user']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
