# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('main.views',
    url(r'^errors/access_denied/$', TemplateView.as_view(template_name='main/access_denied.html'), name='access_denied'),
    url(r'^accounts/became_an_author/$', 'became_an_author', name='became_an_author'),
    url(r'^contact/$', 'contact', name='contact'),

    url(r'^testsimple/$', 'testsimple', name='test'),
    url(r'^testcreate/$', 'testcreate', name='simple'),
    url(r'^welcome/$', 'welcome', name='welcome'),
)
       
