# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url

from views import LinkListView, NewLinkView

urlpatterns = patterns('kolabria.links.views',
                       url(r'^$', LinkListView.as_view(), name='index'),
                       url(r'^new/$', NewLinkView.as_view(), name='new')
)
