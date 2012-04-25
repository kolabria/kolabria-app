from mongoengine.django.auth import User

from kolabria.walls.models import Wall
from kolabria.appliance.models import Box

from django.forms.formsets import formset_factory
from django.utils.safestring import mark_safe 
from django import forms


class UnsubWallForm(forms.Form):
    wid = forms.CharField(widget=forms.HiddenInput, required=False)

class PubWallForm(forms.Form):
    wid = forms.CharField(widget=forms.HiddenInput)

