# -*- coding: utf-8 -*-

from django.forms import ModelForm

from kolabria.links.models import Link


class LinkForm(ModelForm):
    class Meta:
        model = Link
        
        fields = ('title', 'href', 'description')
