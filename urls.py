# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

# STATIC and MEDIA files
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#from kolabria.main.feeds import RSS_URLS
#from kolabria.main.sitemaps import SITEMAPS_URLS
#urlpatterns = SITEMAPS_URLS 
#urlpatterns += RSS_URLS


urlpatterns = patterns('',
    url(r'^links/', include('links.urls', namespace='links')),
    #    url(r'^polls/', include('kolabria.polls.urls', namespace='polls')),
    url(r'^accounts/', include('users.urls', namespace='users')),
    url(r'^accounts/create/$', 'main.views.create_account'),
    url(r'^accounts/welcome/$', 'main.views.welcome'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/$', 'main.views.signup'),
    
    url(r'^create/$', 'main.views.create'),
    url(r'', include('walls.urls')),
    url(r'^', include('main.urls', namespace='main')),
    url(r'^', include('posts.urls', namespace='posts')),
#    url(r'', include('kolabria.walls.appliance.urls')),
    url(r'^', 'main.views.home'),
#    url(r'^public/$', public),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
