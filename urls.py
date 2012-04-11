# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

# STATIC ve MEDIA dosyaları için

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from kolabria.main.feeds import RSS_URLS
from kolabria.main.sitemaps import SITEMAPS_URLS


urlpatterns = SITEMAPS_URLS 
urlpatterns += RSS_URLS


urlpatterns += patterns('',
    url(r'^links/', include('kolabria.links.urls', namespace='links')),
    url(r'^polls/', include('kolabria.polls.urls', namespace='polls')),
    url(r'^accounts/', include('kolabria.users.urls', namespace='users')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('kolabria.main.urls')),
    url(r'^', include('kolabria.posts.urls', namespace='posts')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
