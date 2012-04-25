# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm, TextInput, SlugField, IntegerField

from django.contrib.auth.models import User
from datetime import datetime


class Profile(models.Model):
    """
    User profile model 
    web_site, about, city, user
    """
    user = models.OneToOneField(User, verbose_name='Profile')
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


class Account(models.Model):
    """
    Corporate Account model in django to represent Company objects
    """
    STATUS_CHOICES = (
        (u'Active', u'Active'),
        (u'Inactive', u'Inactive'),
    )

    name = models.CharField("Company Name", max_length=30)
    slug = models.SlugField("Company Subdomain", max_length=30)
    box_count = models.IntegerField("Number of Appliances")
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


class AccountCreationForm(ModelForm):
    class Meta:
        model = Account
