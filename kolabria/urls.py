from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('kolabria.apps.site.urls', namespace='site')),
    url(r'^', include('kolabria.apps.account.urls', namespace='account')),
    url(r'^account/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
